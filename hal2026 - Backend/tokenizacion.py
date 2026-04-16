"""
Fase 1 – Tokenización.

Divide un Markdown generado por MinerU en bloques atómicos:
  'header'  → líneas con # / ## / ###
  'formula' → bloques $$...$$  (pueden ser multilínea)
  'image'   → líneas con ![...](...)
  'text'    → todo lo demás (párrafos)
"""

import re
from dataclasses import dataclass
from typing import List


@dataclass
class Block:
    texto: str
    tipo: str  # 'header' | 'formula' | 'image' | 'text'


def tokenizar(markdown: str) -> List[Block]:
    """
    Divide el markdown en bloques atómicos sin romper ningún elemento
    estructural.  Orden de prioridad:
      1. Fórmulas en bloque  $$...$$  (pueden ser multilínea)
      2. Imágenes            ![...](...) en su propia línea
      3. Encabezados         # / ## / ### al inicio de línea
      4. Párrafos de texto   todo lo demás
    """
    bloques: List[Block] = []

    # Primer corte: separar fórmulas en bloque (multilínea)
    segmento = re.split(r'(\$\$[\s\S]*?\$\$)', markdown)

    for seg in segmento:
        if seg.startswith('$$'):
            text = seg.strip()
            if text:
                bloques.append(Block(texto=text, tipo='formula'))
            continue

        # Dentro de cada segmento sin fórmulas, procesar línea a línea
        lineaPendiente: List[str] = []

        for linea in seg.splitlines():
            stripped = linea.strip()

            if re.match(r'^#{1,3}\s+\S', stripped):          # encabezado
                limpiarTexto(lineaPendiente, bloques)
                bloques.append(Block(texto=stripped, tipo='header'))

            elif re.match(r'^!\[', stripped):                 # imagen
                limpiarTexto(lineaPendiente, bloques)
                bloques.append(Block(texto=stripped, tipo='image'))

            else:
                lineaPendiente.append(linea)

        limpiarTexto(lineaPendiente, bloques)

    return bloques


def limpiarTexto(lines: List[str], bloques: List[Block]) -> None:
    """Convierte las líneas acumuladas en un bloque de texto y limpia la lista."""
    text = '\n'.join(lines).strip()
    if text:
        bloques.append(Block(texto=text, tipo='text'))
    lines.clear()


def bloquesATexto(bloques: List[Block]) -> str:
    """Convierte una lista de bloques a texto plano separado por doble salto."""
    return '\n\n'.join(b.texto for b in bloques)
