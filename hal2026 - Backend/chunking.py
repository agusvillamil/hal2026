"""
API pública de chunking semántico para Markdown generado por MinerU.

Pipeline:
  tokenizacion  → bloques atómicos (header / formula / image / text)
  agrupacion    → grupos de bloques por tamaño
  procesado     → correcciones estructurales (headers huérfanos, imágenes, fórmulas)
  superposicion → overlap configurable entre chunks contiguos
"""

import re
from pathlib import Path
from typing import List

from conseguirRutas import conseguirRutasPDF
from tokenizacion import tokenizar, bloquesATexto
from agrupacion import agruparEnChunks
from procesado import arreglarEncabezadosSolos, arreglarContextoImagenes, deduplicarFormulas
from superposicion import aplicarSuperposicion
from enriquecimiento import enriquecerChunk

# ── Parámetros por defecto ────────────────────────────────────────────────────
TAMANIO_CHUNK = 1500   # caracteres
SUPERPOSICION = 0.15   # 15 %

SEPARADOR = '─' * 60
PATRON_ARCHIVO = re.compile(
    r'MinerU_markdown_\w+-(\d+)-(.+?)-(\d{3})-(\d{3})_\d+\.md$'
)
DIR_CHUNKS = Path(__file__).parent / 'Libros' / 'Libros_Chunks'


def nombreTxt(ruta: str) -> Path:
    nombre = Path(ruta).name
    m = PATRON_ARCHIVO.search(nombre)
    if m:
        num, tema, comienzo, final = m.group(1), m.group(2), int(m.group(3)), int(m.group(4))
        return DIR_CHUNKS / f'Ochoa {num} {tema} {comienzo}-{final} - Dividido en chunks.txt'
    return DIR_CHUNKS / f'{Path(ruta).stem} - Dividido en chunks.txt'


def guardarChunks(ruta: str, chunks: List[str]) -> None:
    rutaTxt = nombreTxt(ruta)
    if rutaTxt.exists():
        return
    DIR_CHUNKS.mkdir(parents=True, exist_ok=True)
    lineas = [f'Archivo  : {ruta}\nChunks   : {len(chunks)}\n']
    for i, chunk in enumerate(chunks, 1):
        lineas.append(f'\n{SEPARADOR}\nChunk {i} ({len(chunk)} chars)\n{SEPARADOR}\n{chunk}\n')
    rutaTxt.write_text(''.join(lineas), encoding='utf-8')
    print(f'  → Guardado: {rutaTxt.name}')


def chunkear(
    ruta: str,
    tamanioChunk: int       = TAMANIO_CHUNK,
    ratio: float            = SUPERPOSICION,
    enriquecer: bool        = True,
) -> List[str]:
    """
    Lee un archivo Markdown generado por MinerU y devuelve una lista
    de chunks semánticos con overlap configurable.

    Args:
        ruta:               Ruta al archivo .md
        tamanioChunk:       Tamaño máximo de cada chunk en caracteres
        ratio:              Fracción del chunk anterior que se repite (0–1)
        enriquecer:         Si True, reemplaza imágenes por descripciones de Gemini

    Returns:
        Lista de strings, cada uno listo para ser indexado en el RAG.
    """
    markdown = Path(ruta).read_text(encoding='utf-8')

    bloques      = tokenizar(markdown)
    gruposChunks = agruparEnChunks(bloques, tamanioChunk)
    gruposChunks = arreglarEncabezadosSolos(gruposChunks)
    gruposChunks = arreglarContextoImagenes(gruposChunks)
    gruposChunks = deduplicarFormulas(gruposChunks)

    texto = [bloquesATexto(g) for g in gruposChunks if g]
    texto = aplicarSuperposicion(texto, ratio)
    texto = [t for t in texto if t.strip()]

    if enriquecer:
        texto = [enriquecerChunk(t) for t in texto]

    guardarChunks(ruta, texto)
    return texto


# ── Ejemplo de uso ────────────────────────────────────────────────────────────

if __name__ == '__main__':
    rutas = conseguirRutasPDF()
    print(f'Archivos encontrados: {len(rutas)}\n')
    
    chunks = chunkear(rutas[0])
    print(f'Archivo  : {rutas[0]}')
    print(f'Chunks   : {len(chunks)}\n')

    for i, chunk in enumerate(chunks):
        print(f'{"─" * 60}')
        print(f'Chunk {i + 1} ({len(chunk)} chars)')
        print(f'{"─" * 60}')
        print(chunk)
        print()
