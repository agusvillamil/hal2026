"""
Enriquecimiento de chunks mediante visión de Llama 4 Scout (Groq).

Recibe un chunk (string Markdown) que puede contener una o más etiquetas
![image](url).  Para cada imagen descarga el contenido, la codifica en
base64 y la describe con Groq, sustituyendo el tag por la descripción.

Dependencias: groq, requests, python-dotenv
"""

import base64
import os
import re
from pathlib import Path
from time import sleep

import requests
from dotenv import load_dotenv
from groq import Groq

load_dotenv(dotenv_path=Path(__file__).parent.parent / '.env')

cliente = Groq(api_key=os.getenv('GROQ_API_KEY'))
MODELO = 'meta-llama/llama-4-scout-17b-16e-instruct'

# Regex que captura cualquier ![image](url) dentro del chunk
ETIQUETA_IMG = re.compile(r'!\[image\]\((https?://[^\)]+)\)')

PROMPT = (
    'Eres un experto en física. '
    'Describe la imagen de forma técnica y concisa (máx. 3 oraciones): '
    'menciona vectores, fuerzas, ejes, puntos de aplicación o cualquier '
    'elemento relevante visible. No uses Markdown, solo texto plano. Responde en español.'
)


def describirImagen(url: str) -> str:
    """Descarga la imagen, la codifica en base64 y consulta Groq.

    Reintenta automáticamente ante errores 429 (rate limit), esperando
    el tiempo indicado por la propia respuesta.
    """
    http = requests.get(url, timeout=15)
    http.raise_for_status()

    # Groq vision API requiere imagen en base64 con su media type
    tipoMedia = http.headers.get('Content-Type', 'image/jpeg').split(';')[0]
    b64 = base64.b64encode(http.content).decode('utf-8')
    dataURL = f'data:{tipoMedia};base64,{b64}'

    reintentoMax = 3
    for intento in range(reintentoMax):
        try:
            respuesta = cliente.chat.completions.create(
                model=MODELO,
                messages=[{
                    'role': 'user',
                    'content': [
                        {'type': 'text',        'text': PROMPT},
                        {'type': 'image_url',   'image_url': {'url': dataURL}},
                    ],
                }],
                max_tokens=256,
            )
            return respuesta.choices[0].message.content.strip()
        except Exception as e:
            mensaje = str(e)
            if '429' in mensaje:
                m = re.search(r'retry[^\d]*(\d+)', mensaje, re.IGNORECASE)
                espera = int(m.group(1)) + 2 if m else 60
                print(f'[enriquecimiento] Rate limit, reintento {intento + 1}/{reintentoMax} en {espera}s...')
                sleep(espera)
            else:
                raise

    raise RuntimeError(f'Groq no respondió tras {reintentoMax} reintentos para {url}')


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
