"""
Enriquecimiento de chunks mediante visión de Llama 4 Scout (Groq).

Recibe un chunk (string Markdown) que puede contener una o más etiquetas
![image](url).  Para cada imagen descarga el contenido, la codifica en
base64 y la describe con Groq, sustituyendo el tag por la descripción.

Dependencias: groq, requests, python-dotenv, modelos
"""

import base64
import re

import requests

from modelos import llamarGroq, MODELO_GROQ_VIS

# Regex que captura cualquier ![image](url) dentro del chunk
ETIQUETA_IMG = re.compile(r'!\[image\]\((https?://[^\)]+)\)')

PROMPT = (
    'Eres un experto en física. '
    'Describe la imagen de forma técnica y concisa (máx. 3 oraciones): '
    'menciona vectores, fuerzas, ejes, puntos de aplicación o cualquier '
    'elemento relevante visible. No uses Markdown, solo texto plano. Responde en español.'
)


def describirImagen(url: str) -> str:
    """Descarga la imagen, la codifica en base64 y consulta Groq vision.

    Los reintentos ante 429 son manejados por llamarGroq en modelos.py.
    """
    http = requests.get(url, timeout=15)
    http.raise_for_status()

    tipoMedia = http.headers.get('Content-Type', 'image/jpeg').split(';')[0]
    b64 = base64.b64encode(http.content).decode('utf-8')
    dataURL = f'data:{tipoMedia};base64,{b64}'

    mensajes = [{
        'role': 'user',
        'content': [
            {'type': 'text',      'text': PROMPT},
            {'type': 'image_url', 'image_url': {'url': dataURL}},
        ],
    }]

    descripcion = llamarGroq(mensajes, modelo=MODELO_GROQ_VIS, max_tokens=256, temperature=0.2)
    print('  [Groq] Imagen descrita')
    return descripcion.strip()


def enriquecerChunk(chunk: str) -> str:
    """
    Reemplaza cada tag ![image](url) dentro de `chunk` por una descripción
    textual generada por Llama 4 Scout via Groq.

    Args:
        chunk: Texto Markdown de un chunk, posiblemente con imágenes.

    Returns:
        El mismo chunk con los tags de imagen sustituidos por
        '[Descripción de imagen: <descripcion>]'.
    """
    def reemplazar(match: re.Match) -> str:
        url = match.group(1)
        try:
            descripcion = describirImagen(url)
            return f'[Descripción de imagen: {descripcion}]'
        except Exception as e:
            print(f'[enriquecimiento] ERROR al describir imagen {url}: {e}')
            return match.group(0)

    return ETIQUETA_IMG.sub(reemplazar, chunk)
