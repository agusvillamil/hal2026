import os
import re
from pathlib import Path

import chromadb
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from modelos import llamarRespuesta

load_dotenv(dotenv_path=Path(__file__).parent.parent / '.env')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["*"],
)

N_RESULTADOS = 5

clienteChroma = chromadb.PersistentClient(path='./chroma_db')
coleccion = clienteChroma.get_or_create_collection(
    name='fisica_chunks',
    metadata={'hnsw:space': 'cosine'},
)

PROMPT_SISTEMA = (
    'Eres un asistente experto en Física I universitaria. '
    'Responde la pregunta del usuario basándote ÚNICAMENTE en los fragmentos '
    'de contexto proporcionados. En caso de que el contexto no contenga información suficiente '
    'intenta inferir la respuesta usando tu conocimiento general de física'
    'para responder, indícalo claramente y responde que no hay suficiente información. '
    'Usa notación LaTeX para fórmulas matemáticas: '
    '$...$ para fórmulas en línea y $$...$$ para fórmulas en bloque. '
    'Nunca uses \\(...\\) ni \\[...\\]. '
    'Nunca envuelvas fórmulas en bloques de código (```), ni siquiera con ```latex o ```math; '
    'usa solo $...$ o $$...$$. '
    'Nunca dejes delimitadores $ o $$ sin cerrar — cada $ de apertura debe tener su $ de cierre en el mismo párrafo. '
    'Si una fórmula contiene texto con unidades (m/s, km/h, etc.), incluí las unidades DENTRO de la fórmula usando \\text{...} o \\,\\mathrm{...}, no las dejes mezcladas con texto plano. '
    'Responde en español. Responde de manera concisa'
)


class Pregunta(BaseModel):
    mensaje: str


@app.post('/chat')
def chat(pregunta: Pregunta):
    # 1. Buscar chunks similares en ChromaDB
    resultados = coleccion.query(
        query_texts=[pregunta.mensaje],
        n_results=N_RESULTADOS,
        include=['documents', 'metadatas'],
    )

    documentos = resultados['documents'][0]
    metadatas  = resultados['metadatas'][0]

    if not documentos:
        raise HTTPException(status_code=404, detail='Sin resultados en la base de datos.')

    # 2. Construir bloque de contexto con fuente de cada chunk
    bloques = []
    for doc, meta in zip(documentos, metadatas):
        fuente = f"{meta.get('topic', '?')} (p. {meta.get('page_start', '?')}–{meta.get('page_end', '?')})"
        bloques.append(f'[{fuente}]\n{doc}')
    contexto = '\n\n---\n\n'.join(bloques)

    # 3. Enviar pregunta + contexto al modelo configurado
    mensajes = [
        {'role': 'system', 'content': PROMPT_SISTEMA},
        {'role': 'user',   'content': f'Contexto:\n{contexto}\n\nPregunta: {pregunta.mensaje}'},
    ]
    texto = llamarRespuesta(mensajes, max_tokens=4096, temperature=0.2)

    texto_raw = texto

    # Desenvuelve fences de código que contengan LaTeX (```latex, ```math, ```tex o ``` con \frac/\begin/etc.)
    def _desenvolver_fence(match: re.Match) -> str:
        lang = (match.group(1) or '').lower()
        cuerpo = match.group(2)
        if lang in ('latex', 'math', 'tex'):
            return f'$$\n{cuerpo.strip()}\n$$'
        if re.search(r'\\(frac|begin|sqrt|sum|int|vec|hat|alpha|beta|gamma|theta|omega|cdot|times)\b|\^\{|_\{', cuerpo):
            return f'$$\n{cuerpo.strip()}\n$$'
        return match.group(0)

    texto = re.sub(r'```(\w+)?\s*\n?(.+?)\n?```', _desenvolver_fence, texto, flags=re.DOTALL)

    # Convierte delimitadores \[...\] y \(...\) a $$...$$ y $...$
    texto = re.sub(r'\\\[(.+?)\\\]', r'$$\1$$', texto, flags=re.DOTALL)
    texto = re.sub(r'\\\((.+?)\\\)', r'$\1$', texto, flags=re.DOTALL)

    print(f"\n{'='*60}")
    print(f"[PROMPT SISTEMA]\n{PROMPT_SISTEMA}")
    print(f"[CONTEXTO]\n{contexto}")
    print(f"[PREGUNTA] {pregunta.mensaje}")
    print(f"[RESPUESTA RAW]\n{texto_raw}")
    print(f"[RESPUESTA PROCESADA]\n{texto}")
    print(f"{'='*60}\n")

    return {'respuesta': texto.strip()}
