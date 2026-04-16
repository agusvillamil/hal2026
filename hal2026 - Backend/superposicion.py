"""
Fase 4 – Superposición (overlap).

Antepone el final del chunk anterior al inicio del chunk actual para
que el modelo RAG tenga contexto en los límites de cada fragmento.
El punto de corte se ajusta al inicio de una oración completa.
"""

import re
from typing import List


def aplicarSuperposicion(texts: List[str], ratio: float) -> List[str]:
    """
    Antepone el último ``ratio * len(prev)`` caracteres del chunk
    anterior al chunk actual.

    El punto de corte retrocede hasta el inicio de una oración para
    no arrancar a mitad de frase.

    Args:
        texts: Lista de chunks como strings.
        ratio: Fracción del chunk anterior a reutilizar (0–1).

    Returns:
        Nueva lista de chunks con overlap aplicado.
    """
    if not texts:
        return texts

    result = [texts[0]]

    for i in range(1, len(texts)):
        prev        = texts[i - 1]
        longitudSuperposicion = int(len(prev) * ratio)

        if longitudSuperposicion <= 0:
            result.append(texts[i])
            continue

        cola = prev[-longitudSuperposicion:]

        # Retroceder hasta el inicio de una oración completa
        m = re.search(r'(?<=[.!?])\s+\S', cola)
        if m:
            cola = cola[m.start() + len(m.group()) - 1:]

        result.append(cola.strip() + '\n\n' + texts[i])

    return result
