"""
Modelos de lenguaje con rotación automática por pool.

Tres pools con fallback automático ante rate limits (429):
  POOL_VISION    → descripción de imágenes (modelos multimodales)
  POOL_METADATOS → extracción de metadatos JSON (modelos rápidos de texto)
  POOL_RESPUESTA → respuesta al usuario con contexto RAG (modelos potentes)

Proveedores: groq, gemini, nvidia  (todos via API OpenAI-compatible)
API keys via variables de entorno:
  GROQ_API_KEY, GEMINI_API_KEY, NVIDIA_API_KEY

Dependencia: pip install openai
"""

import os
from time import sleep
from typing import List

from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

# ── Pools de modelos ───────────────────────────────────────────────────────────
# Cada entrada es (proveedor, modelo_id).
# La rotación va de arriba hacia abajo: ante un rate limit, pasa al siguiente.
# Cuando llega al final vuelve al inicio tras una espera.

POOL_VISION: List[tuple] = [
    ('groq',   'meta-llama/llama-4-scout-17b-16e-instruct'),
    ('gemini', 'gemini-2.5-flash'),
    ('nvidia', 'nvidia/nemotron-nano-12b-v2-vl'),
    ('gemini', 'gemini-2.0-flash'),             # fallback: cuota generosa
]

POOL_METADATOS: List[tuple] = [
    ('groq', 'llama-3.1-8b-instant'),
    ('groq', 'gemma2-9b-it'),                   # fallback: muy rápido para JSON
]

POOL_RESPUESTA: List[tuple] = [
    ('groq',   'llama-3.3-70b-versatile'),
    ('groq',   'openai/gpt-oss-120b'),
    ('groq',   'qwen/qwen3-32b'),
    ('gemini', 'gemini-2.5-pro'),
    ('groq',   'deepseek-r1-distill-llama-70b'), # fallback: razonamiento fuerte
]

_POOLS = {
    'vision':    POOL_VISION,
    'metadatos': POOL_METADATOS,
    'respuesta': POOL_RESPUESTA,
}

# Índice actual por pool — se avanza ante cada rate limit, se mantiene en éxito
_idx_pool: dict = {nombre: 0 for nombre in _POOLS}

# ── Constantes de compatibilidad ───────────────────────────────────────────────
MODELO_GROQ     = POOL_RESPUESTA[0][1]
MODELO_GROQ_VIS = POOL_VISION[0][1]

# ── Clientes lazy (uno por proveedor) ─────────────────────────────────────────
_BASES = {
    'groq':   'https://api.groq.com/openai/v1',
    'gemini': 'https://generativelanguage.googleapis.com/v1beta/openai/',
    'nvidia': 'https://integrate.api.nvidia.com/v1',
}
_KEYS = {
    'groq':   'GROQ_API_KEY',
    'gemini': 'GEMINI_API_KEY',
    'nvidia': 'NVIDIA_API_KEY',
}
_clientes: dict = {}


def _cliente(proveedor: str):
    if proveedor not in _clientes:
        try:
            from openai import OpenAI
        except ImportError:
            raise ImportError('Instalar: pip install openai')
        api_key = os.getenv(_KEYS[proveedor], '')
        if not api_key:
            raise EnvironmentError(
                f'Variable de entorno {_KEYS[proveedor]} no configurada'
            )
        _clientes[proveedor] = OpenAI(base_url=_BASES[proveedor], api_key=api_key)
    return _clientes[proveedor]


# ── Motor de rotación ──────────────────────────────────────────────────────────

def _es_rate_limit(exc: Exception) -> bool:
    s = str(exc).lower()
    return '429' in s or 'rate_limit' in s or 'rate limit' in s


def _llamar_uno(proveedor: str, modelo: str, mensajes: list,
                max_tokens: int, temperature: float) -> str:
    resp = _cliente(proveedor).chat.completions.create(
        model=modelo,
        messages=mensajes,
        max_tokens=max_tokens,
        temperature=temperature,
    )
    return resp.choices[0].message.content


def _llamar_pool(nombre: str, mensajes: list,
                 max_tokens: int, temperature: float) -> str:
    """
    Recorre el pool rotando ante rate limits.
    Primera vuelta: sin espera. Segunda vuelta: tras 60 s de pausa.
    Se queda en el modelo que funcionó para la próxima llamada.
    """
    pool = _POOLS[nombre]
    n = len(pool)

    for vuelta in range(2):
        inicio = _idx_pool[nombre]
        for i in range(n):
            idx = (inicio + i) % n
            proveedor, modelo = pool[idx]
            tag = f'{proveedor}/{modelo.split("/")[-1]}'
            try:
                resultado = _llamar_uno(proveedor, modelo, mensajes, max_tokens, temperature)
                _idx_pool[nombre] = idx
                print(f'  [{tag}] OK')
                return resultado
            except Exception as e:
                if _es_rate_limit(e):
                    siguiente = pool[(idx + 1) % n]
                    print(f'  [{tag}] Rate limit → rotando a {siguiente[0]}/{siguiente[1].split("/")[-1]}')
                    _idx_pool[nombre] = (idx + 1) % n
                    continue
                raise

        if vuelta == 0:
            print(f'  [pool:{nombre}] Todos los modelos en rate limit, esperando 60 s...')
            sleep(60)

    raise RuntimeError(f'Pool "{nombre}": todos los modelos agotaron su rate limit.')


# ── API pública ────────────────────────────────────────────────────────────────

def avanzarPool(nombre: str) -> None:
    """Avanza manualmente el pool al siguiente modelo (usar ante errores de aplicación)."""
    pool = _POOLS.get(nombre)
    if not pool:
        return
    _idx_pool[nombre] = (_idx_pool[nombre] + 1) % len(pool)
    proveedor, modelo = pool[_idx_pool[nombre]]
    print(f'  [pool:{nombre}] → {proveedor}/{modelo.split("/")[-1]}')


def llamarVision(mensajes: list, max_tokens: int = 256, temperature: float = 0.2) -> str:
    """Describe una imagen usando el pool de visión con rotación automática."""
    return _llamar_pool('vision', mensajes, max_tokens, temperature)


def llamarMetadatos(mensajes: list, max_tokens: int = 128, temperature: float = 0) -> str:
    """Extrae metadatos JSON usando el pool de extracción con rotación automática."""
    return _llamar_pool('metadatos', mensajes, max_tokens, temperature)


def llamarRespuesta(mensajes: list, max_tokens: int = 1024, temperature: float = 0.2) -> str:
    """Genera respuesta al usuario usando el pool de respuesta con rotación automática."""
    return _llamar_pool('respuesta', mensajes, max_tokens, temperature)


# ── Aliases de compatibilidad con código anterior ──────────────────────────────

def llamarModelo(mensajes: list, modelo_groq: str = None,  # noqa: ARG001
                 max_tokens: int = 1024, temperature: float = 0.2) -> str:
    """Compatibilidad: usa el pool de respuesta."""
    return llamarRespuesta(mensajes, max_tokens=max_tokens, temperature=temperature)


def llamarGroq(mensajes: list, modelo: str = None, max_tokens: int = 1024,
               temperature: float = 0.2, intentos: int = 3) -> str:  # noqa: ARG001
    """Compatibilidad: rutas al pool correcto según si el modelo es de visión."""
    if modelo and modelo == MODELO_GROQ_VIS:
        return llamarVision(mensajes, max_tokens=max_tokens, temperature=temperature)
    return llamarRespuesta(mensajes, max_tokens=max_tokens, temperature=temperature)
