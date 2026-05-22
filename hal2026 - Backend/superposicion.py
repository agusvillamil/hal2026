"""
Fase 4 – Superposición (overlap) consciente de bloques.

Antepone los últimos bloques del chunk anterior al inicio del chunk
actual, sin romper jamás un bloque por la mitad. Garantiza que el
overlap nunca arranque a mitad de fórmula, oración, header o imagen.
"""

from typing import List

from tokenizacion import Block, bloquesATexto


def aplicarSuperposicion(grupos: List[List[Block]], ratio: float) -> List[str]:
    """
    Anexa al inicio de cada chunk los últimos bloques del chunk anterior
    cuya longitud combinada quepa en ``ratio * len(prev_texto)``.

    Si el primer bloque del chunk actual es ``ejercicio_header``, no se
    aplica overlap (límite semántico duro).

    Args:
        grupos: Lista de chunks, cada uno como lista de bloques atómicos.
        ratio:  Fracción del chunk anterior a reutilizar (0–1).

    Returns:
        Lista de strings (texto plano de cada chunk con overlap aplicado).
    """
    if not grupos:
        return []

    resultado: List[str] = [bloquesATexto(grupos[0])]

    for i in range(1, len(grupos)):
        actual = grupos[i]

        if not actual:
            continue

        # Ejercicio: límite duro, no contaminar con cola previa.
        if actual[0].tipo == 'ejercicio_header':
            resultado.append(bloquesATexto(actual))
            continue

        prev = grupos[i - 1]
        textoPrev = bloquesATexto(prev)
        presupuesto = int(len(textoPrev) * ratio)

        if presupuesto <= 0 or not prev:
            resultado.append(bloquesATexto(actual))
            continue

        # Recolectar bloques del final hacia atrás hasta agotar presupuesto.
        # Nunca se corta un bloque: si no entra entero, se descarta.
        bloquesOverlap: List[Block] = []
        usado = 0
        for bloque in reversed(prev):
            costo = len(bloque.texto) + 2  # +2 por separador '\n\n'
            if usado + costo > presupuesto:
                break
            bloquesOverlap.insert(0, bloque)
            usado += costo

        # Dedup: si el primer bloque del chunk actual es idéntico al
        # último del overlap (caso típico tras procesado.deduplicarFormulas),
        # evitar repetirlo.
        if (bloquesOverlap
                and actual
                and bloquesOverlap[-1].texto.strip() == actual[0].texto.strip()):
            bloquesOverlap.pop()

        if bloquesOverlap:
            combinado = bloquesATexto(bloquesOverlap) + '\n\n' + bloquesATexto(actual)
        else:
            combinado = bloquesATexto(actual)

        resultado.append(combinado)

    return resultado
