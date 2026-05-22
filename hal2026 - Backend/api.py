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
    'Nunca uses \\(...\\) ni \\[...\\]. Responde en español. Responde de manera concisa'
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
    texto = llamarRespuesta(mensajes, max_tokens=1024, temperature=0.2)

    texto = re.sub(r'\\\[(.+?)\\\]', r'$$\1$$', texto, flags=re.DOTALL)
    texto = re.sub(r'\\\((.+?)\\\)', r'$\1$', texto, flags=re.DOTALL)

    print(f"\n{'='*60}")
    print(f"[PROMPT SISTEMA]\n{PROMPT_SISTEMA}")
    print(f"[CONTEXTO]\n{contexto}")
    print(f"[PREGUNTA] {pregunta.mensaje}")
    print(f"[RESPUESTA RAW]\n{texto}")
    print(f"{'='*60}\n")

    return {'respuesta': texto.strip()}
