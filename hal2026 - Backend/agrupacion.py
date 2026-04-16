"""
Agrupación greedy en chunks.

Toma la lista de bloques atómicos de tokenizacion.py y los agrupa
en listas de bloques cuya longitud combinada no supere tamanioChunk.
Los bloques de texto que por sí solos superen tamanioChunk se dividen
por límites de oración sin romper fórmulas en la misma linea ($...$).
"""

import re
from typing import List

from tokenizacion import Block


def agruparEnChunks(
    bloques: List[Block],
    tamanioChunk: int,
) -> List[List[Block]]:
    """
    Agrupa bloques atómicos hasta llegar a tamanioChunk.
    Si un bloque de texto supera tamanioChunk por sí solo, se divide por
    oraciones (priorizando '. ' y '\\n\\n') sin romper fórmulas inline.
    """
    chunks: List[List[Block]] = []
    actual: List[Block] = []
    largoActual = 0

    def sumarChunk() -> None:
        nonlocal actual, largoActual
        if actual:
            chunks.append(actual)
        actual = []
        largoActual = 0

    for block in bloques:
        blen = len(block.texto)

        # Bloque de texto demasiado grande: dividir por oraciones
        if block.tipo == 'text' and blen > tamanioChunk:
            for sub in dividirPorOraciones(block.texto, tamanioChunk):
                subBloque = Block(texto=sub, tipo='text')
                subLargo   = len(sub)
                if largoActual + subLargo > tamanioChunk:
                    sumarChunk()
                actual.append(subBloque)
                largoActual += subLargo + 2
            continue

        # Bloque no-texto o texto pequeño
        if largoActual + blen > tamanioChunk and actual:
            sumarChunk()

        actual.append(block)
        largoActual += blen + 2  # +2 por separador '\n\n'

    sumarChunk()
    return chunks


def dividirPorOraciones(text: str, largoMax: int) -> List[str]:
    """
    Divide texto largo en fragmentos ≤ largoMax respetando límites de oración.
    Separadores en orden de prioridad: '\\n\\n', '. ', '! ', '? '.
    Nunca corta dentro de $…$ (fórmulas inline).
    """
    # Proteger fórmulas inline para que no sean cortadas
    plantillas: List[str] = []

    def protegerMismaLinea(m: re.Match) -> str:
        idx = len(plantillas)
        plantillas.append(m.group(0))
        return f'⟨FORMULA_{idx}⟩'

    protegido = re.sub(r'\$[^$\n]+?\$', protegerMismaLinea, text)

    # Dividir por candidatos de corte
    oraciones = re.split(r'(\n\n|(?<=[.!?])\s+)', protegido)

    fragmentos: List[str] = []
    actual = ''

    for pedazo in oraciones:
        if len(actual) + len(pedazo) <= largoMax:
            actual += pedazo
        else:
            if actual.strip():
                fragmentos.append(actual.strip())
            actual = pedazo

    if actual.strip():
        fragmentos.append(actual.strip())

    # Restaurar fórmulas inline
    def recuperar(s: str) -> str:
        for i, formula in enumerate(plantillas):
            s = s.replace(f'⟨FORMULA_{i}⟩', formula)
        return s

    return [recuperar(f) for f in fragmentos if f.strip()]
