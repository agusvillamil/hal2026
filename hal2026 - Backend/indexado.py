"""
Indexado de chunks en ChromaDB con metadatos estructurales y semánticos.

Pipeline:
  1. Lee todos los archivos .md desde PDF_DIR
  2. Genera chunks con chunking.get_chunks()
  3. Extrae metadatos estructurales del nombre de archivo (MinerU)
  4. Detecta presencia de fórmulas e imágenes en el texto
  5. Extrae metadatos semánticos via Groq (tipo de contenido, conceptos)
  6. Almacena documentos + embeddings + metadatos en ChromaDB persistente

Dependencias: chromadb, sentence-transformers, groq, python-dotenv
"""

import json
import os
import re
from pathlib import Path
from time import sleep
from typing import Optional

import chromadb
from dotenv import load_dotenv
from groq import Groq

from conseguirRutas import conseguirRutasPDF
from chunking import chunkear, nombreTxt, guardarChunks

load_dotenv(dotenv_path=Path(__file__).parent.parent / '.env')

clienteGroq = Groq(api_key=os.getenv('GROQ_API_KEY'))
MODELO = 'llama-3.3-70b-versatile'

# Patrón de nombre de archivo MinerU:
# MinerU_markdown_Ochoa-{num}-{topic}-{start}-{end}_{id}.md
PATRON_ARCHIVO = re.compile(
    r'MinerU_markdown_\w+-(\d+)-(.+?)-(\d{3})-(\d{3})_(\d+)\.md$'
)

PROMPT_METADATOS = (
    'Eres un experto en física universitaria. '
    'Analiza el siguiente fragmento de texto de un libro de Física I y responde '
    'ÚNICAMENTE con un objeto JSON (sin markdown, sin explicaciones) con estos campos:\n'
    '- "tipo_contenido": uno de ["definicion", "teorema", "demostracion", '
    '"ejemplo", "ejercicio", "introduccion", "otro"]\n'
    '- "conceptos": string con los conceptos físicos clave separados por coma '
    '(máx. 5 conceptos, en español, ej: "fuerza, masa, aceleración")\n\n'
    'Fragmento:\n'
)


def extraerMetadatosArchivo(ruta: str) -> dict:
    """
    Parsea el nombre de archivo MinerU para extraer metadatos estructurales.

    Args:
        ruta: Ruta completa al archivo .md

    Returns:
        Dict con: source, source_path, chapter_num, topic,
                  page_start, page_end, file_id
    """
    nombre = Path(ruta).name
    m = PATRON_ARCHIVO.search(nombre)

    if m:
        return {
            'source':       Path(ruta).stem,
            'source_path':  str(Path(ruta).resolve()),
            'chapter_num':  int(m.group(1)),
            'topic':        m.group(2),
            'page_start':   int(m.group(3)),
            'page_end':     int(m.group(4)),
            'file_id':      m.group(5),
        }

    # Fallback si el nombre no coincide con el patrón esperado
    file_id = Path(ruta).stem.replace(' ', '_')
    return {
        'source':       Path(ruta).stem,
        'source_path':  str(Path(ruta).resolve()),
        'chapter_num':  0,
        'topic':        'desconocido',
        'page_start':   0,
        'page_end':     0,
        'file_id':      file_id,
    }


def extraerMetadatosGroq(chunk: str) -> dict:
    """
    Consulta Groq para extraer tipo de contenido y conceptos físicos del chunk.

    Reintenta ante errores 429. Ante cualquier otro error devuelve valores
    por defecto para no interrumpir el proceso de indexado.

    Args:
        chunk: Texto del chunk a analizar.

    Returns:
        Dict con: tipo_contenido (str), conceptos (str)
    """
    reintentosMax = 3
    for intento in range(reintentosMax):
        try:
            respuesta = clienteGroq.chat.completions.create(
                model=MODELO,
                messages=[{
                    'role': 'user',
                    'content': PROMPT_METADATOS + chunk[:2000],  # limitar tokens
                }],
                max_tokens=128,
                temperature=0,
            )
            texto = respuesta.choices[0].message.content.strip()

            # Eliminar posibles bloques de código markdown si el modelo los agrega
            texto = re.sub(r'^```(?:json)?\s*|\s*```$', '', texto, flags=re.MULTILINE).strip()

            datos = json.loads(texto)
            return {
                'tipo_contenido': str(datos.get('tipo_contenido', 'otro')),
                'conceptos':      str(datos.get('conceptos', '')),
            }

        except Exception as e:
            mensaje = str(e)
            if '429' in mensaje:
                m = re.search(r'retry[^\d]*(\d+)', mensaje, re.IGNORECASE)
                espera = int(m.group(1)) + 2 if m else 60
                print(f'  [groq] Rate limit, reintento {intento + 1}/{reintentosMax} en {espera}s...')
                sleep(espera)
            else:
                print(f'  [groq] Error extrayendo metadatos: {e}')
                return {'tipo_contenido': 'otro', 'conceptos': ''}

    print(f'  [groq] Sin respuesta tras {reintentosMax} reintentos.')
    return {'tipo_contenido': 'otro', 'conceptos': ''}


def leerChunksDesdeTxt(ruta_txt: Path) -> list:
    """
    Lee y devuelve los chunks almacenados en un .txt generado por guardarChunks().

    El formato alterna: header-archivo / "Chunk N" / texto / "Chunk N+1" / texto...
    Al hacer split por el separador (─×60), los textos quedan en índices pares ≥ 2.
    """
    contenido = ruta_txt.read_text(encoding='utf-8')
    partes = contenido.split('─' * 60)
    # partes[0]  = cabecera (Archivo / Chunks)
    # partes[1]  = "Chunk 1 (X chars)"   ← descartar
    # partes[2]  = texto chunk 1          ← guardar
    # partes[3]  = "Chunk 2 (Y chars)"   ← descartar
    # partes[4]  = texto chunk 2          ← guardar  …
    return [partes[i].strip() for i in range(2, len(partes), 2) if partes[i].strip()]


def indexarTodos(
    dirPersistente: str    = './chroma_db',
    coleccion: str      = 'fisica_chunks',
    tamanioChunk: int     = 1500,
    ratio: float = 0.15,
    enriquecer: bool    = True,
    extraerConGroq: bool = True,
) -> chromadb.Collection:
    """
    Procesa todos los archivos .md y almacena sus chunks en ChromaDB.

    Soporta indexado incremental: omite chunks cuyo ID ya exista en la
    colección, evitando duplicados al re-ejecutar el script.

    Args:
        dirPersistente:      Ruta donde ChromaDB persiste los datos.
        coleccion:        Nombre de la colección en ChromaDB.
        tamanioChunk:       Tamaño máximo de chunk en caracteres.
        ratio:    Fracción de overlap entre chunks contiguos.
        enriquecer:       Si True, describe imágenes con Groq vision.
        extraerConGroq: Si True, extrae tipo_contenido y conceptos con Groq.

    Returns:
        La colección de ChromaDB con todos los chunks indexados.
    """
    rutas = conseguirRutasPDF()
    print(f'Archivos encontrados: {len(rutas)}\n')

    clienteChroma = chromadb.PersistentClient(path=dirPersistente)
    coleccionDatabase = clienteChroma.get_or_create_collection(
        name=coleccion,
        metadata={'hnsw:space': 'cosine'},
    )

    totalNuevos = 0

    for i, ruta in enumerate(rutas, 1):
        metaArchivo = extraerMetadatosArchivo(ruta)
        idArchivo      = metaArchivo['file_id']
        tema        = metaArchivo['topic']

        print(f'[{i}/{len(rutas)}] Ochoa-{metaArchivo["chapter_num"]}-{tema}')

        # Si el .txt existe, el chunking completó correctamente en una ejecución
        # anterior → leer chunks desde disco sin llamar Groq para imágenes.
        # Si no existe → pipeline completo (Groq vision + guardar .txt).
        ruta_txt = nombreTxt(ruta)
        if ruta_txt.exists():
            chunks = leerChunksDesdeTxt(ruta_txt)
        else:
            chunks = chunkear(ruta, tamanioChunk, ratio, enriquecer)

        # Chequeo incremental por chunk ID: omite los ya indexados,
        # retoma los faltantes aunque el archivo esté parcialmente indexado.
        existentes = coleccionDatabase.get(where={'file_id': idArchivo}, include=[])
        ids_existentes = set(existentes['ids'])

        if len(ids_existentes) == len(chunks):
            print(f'  → Completo ({len(chunks)} chunks), saltando\n')
            continue

        docs, metas, ids = [], [], []

        for idx, chunk in enumerate(chunks):
            docID = f'{idArchivo}_{idx:04d}'

            if docID in ids_existentes:
                continue

            # Metadatos detectados desde el texto (sin API)
            tieneFormulas  = '$$' in chunk
            tieneImagenes  = '[Descripción de imagen:' in chunk

            meta = {
                **metaArchivo,
                'chunk_index':     idx,
                'char_count':      len(chunk),
                'tiene_formulas':  tieneFormulas,
                'tiene_imagenes':  tieneImagenes,
            }

            if extraerConGroq:
                metadataGroq = extraerMetadatosGroq(chunk)
                meta.update(metadataGroq)
            else:
                meta['tipo_contenido'] = 'otro'
                meta['conceptos']      = ''

            docs.append(chunk)
            metas.append(meta)
            ids.append(docID)

        if docs:
            coleccionDatabase.add(documents=docs, metadatas=metas, ids=ids)
            totalNuevos += len(docs)
            print(f'  → {len(docs)} chunks indexados\n')

    total = coleccionDatabase.count()
    print(f'─' * 50)
    print(f'Chunks nuevos esta ejecución : {totalNuevos}')
    print(f'Total en colección           : {total}')

    return coleccionDatabase


if __name__ == '__main__':
    indexarTodos()
