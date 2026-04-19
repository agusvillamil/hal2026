"""
Abstracción de modelos de lenguaje: Groq y modelos locales via Ollama.

Configuración via variables de entorno:
  MODELO_PROVEEDOR   'groq' (defecto) | 'local'
  MODELO_GROQ        modelo Groq para texto (defecto: llama-3.3-70b-versatile)
  MODELO_GROQ_VISION modelo Groq para visión (defecto: meta-llama/llama-4-scout-17b-16e-instruct)
  MODELO_LOCAL       modelo Ollama (defecto: gemma4)
"""

import os
import re
from time import sleep

from dotenv import load_dotenv
from groq import Groq
import ollama

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

PROVEEDOR       = os.getenv('MODELO_PROVEEDOR', 'groq')
MODELO_GROQ     = os.getenv('MODELO_GROQ', 'llama-3.3-70b-versatile')
MODELO_GROQ_VIS = os.getenv('MODELO_GROQ_VISION', 'meta-llama/llama-4-scout-17b-16e-instruct')
MODELO_LOCAL    = os.getenv('MODELO_LOCAL', 'gemma4')

clienteGroq = None


def _groq() -> Groq:
    global clienteGroq
    if clienteGroq is None:
        clienteGroq = Groq(api_key=os.getenv('GROQ_API_KEY'))
    return clienteGroq


def llamarGroq(mensajes: list, modelo: str = None, max_tokens: int = 1024,
                temperature: float = 0.2, intentos: int = 3) -> str:
    """Llama a un modelo de Groq. Reintenta automáticamente ante rate limiting (429)."""
    modelo = modelo or MODELO_GROQ
    for intento in range(intentos):
        try:
            resp = _groq().chat.completions.create(
                model=modelo,
                messages=mensajes,
                max_tokens=max_tokens,
                temperature=temperature,
            )
            return resp.choices[0].message.content
        except Exception as e:
            if '429' not in str(e) or intento == intentos - 1:
                raise
            m = re.search(r'retry[^\d]*(\d+)', str(e), re.IGNORECASE)
            espera = int(m.group(1)) + 2 if m else 60
            print(f'  [Groq] Rate limit, reintento {intento + 1}/{intentos} en {espera}s...')
            sleep(espera)
    return ''


def llamarLocal(mensajes: list, modelo: str = None, max_tokens: int = 1024,
                 temperature: float = 0.2) -> str:
    """Llama a un modelo local via Ollama."""
    modelo = modelo or MODELO_LOCAL
    resp = ollama.chat(
        model=modelo,
        messages=mensajes,
        options={'num_predict': max_tokens, 'temperature': temperature},
    )
    return resp['message']['content']


def llamarModelo(mensajes: list, modelo_groq: str = None, max_tokens: int = 1024,
                  temperature: float = 0.2) -> str:
    """Llama a Groq o al modelo local según la variable de entorno MODELO_PROVEEDOR."""
    if PROVEEDOR == 'local':
        return llamarLocal(mensajes, max_tokens=max_tokens, temperature=temperature)
    return llamarGroq(mensajes, modelo=modelo_groq, max_tokens=max_tokens, temperature=temperature)
