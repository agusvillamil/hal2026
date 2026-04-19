import os
from pathlib import Path

import chromadb
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from modelos import llamarModelo

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
    'de contexto proporcionados. Si el contexto no contiene información suficiente '
    'para responder, indícalo claramente. '
    'Usa notación LaTeX para fórmulas matemáticas. Responde en español.'
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
    texto = llamarModelo(mensajes, max_tokens=1024, temperature=0.2)

    return {'respuesta': texto.strip()}
