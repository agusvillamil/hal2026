"""
Fase 3 – Post-procesado estructural.

Aplica cuatro correcciones sobre los grupos de bloques ya agrupados:
  1. arreglarEncabezadosSolos  – mueve headers al inicio del chunk siguiente
  2. arreglarContextoImagenes  – arrastra texto descriptivo junto a la imagen
  3. deduplicarFormulas        – elimina fórmulas idénticas en frontera de chunks
  4. arreglarEjercicios        – fusiona secciones huérfanas de ejercicio con el chunk anterior
"""

import re
from typing import List

from tokenizacion import Block, bloquesATexto

# Ventana de búsqueda de palabras clave antes de una imagen
VENTANA_IMG = 500

PALABRAS_CLAVE_IMG = re.compile(
    r'\b(figura|gráfica|diagrama|imagen|figure|graph|plot|tabla)\b',
    re.IGNORECASE,
)


def arreglarEncabezadosSolos(chunks: List[List[Block]]) -> List[List[Block]]:
    """
    Si un chunk termina en uno o más encabezados o secciones de ejercicio
    sin contenido tras ellos, los mueve al inicio del chunk siguiente.
    Esto evita que '## EJECUCIÓN' quede colgado al final de un chunk
    sin su texto asociado.
    """
    TIPOS_HUERFANOS = ('header', 'ejercicio_seccion')
    for i in range(len(chunks) - 1):
        while chunks[i] and chunks[i][-1].tipo in TIPOS_HUERFANOS:
            huerfano = chunks[i].pop()
            chunks[i + 1].insert(0, huerfano)
    return chunks


def arreglarContextoImagenes(chunks: List[List[Block]]) -> List[List[Block]]:
    """
    Si un chunk comienza con una imagen y los últimos VENTANA_IMG
    caracteres del chunk anterior contienen palabras clave descriptivas
    (figura, gráfica…), arrastra el último bloque de texto anterior
    al inicio del chunk con la imagen.
    """
    for i in range(1, len(chunks)):
        if not chunks[i] or chunks[i][0].tipo != 'image':
            continue

        textoAnterior = bloquesATexto(chunks[i - 1])
        cola = textoAnterior[-VENTANA_IMG:]

        if PALABRAS_CLAVE_IMG.search(cola) and chunks[i - 1]:
            # Buscar hacia atrás el último bloque de texto
            j = len(chunks[i - 1]) - 1
            while j >= 0 and chunks[i - 1][j].tipo != 'text':
                j -= 1
            if j >= 0:
                bloqueContexto = chunks[i - 1].pop(j)
                chunks[i].insert(0, bloqueContexto)

    return chunks


def arreglarEjercicios(chunks: List[List[Block]]) -> List[List[Block]]:
    """
    Si un chunk comienza con una sección de ejercicio (IDENTIFICAR, PLANTEAMIENTO,
    EJECUCIÓN, EVALUACIÓN) sin un ejercicio_header precedente, lo fusiona con el
    chunk anterior para evitar secciones huérfanas.
    """
    resultado: List[List[Block]] = []
    for chunk in chunks:
        if chunk and chunk[0].tipo == 'ejercicio_seccion' and resultado:
            resultado[-1].extend(chunk)
        else:
            resultado.append(chunk)
    return resultado


def deduplicarFormulas(chunks: List[List[Block]]) -> List[List[Block]]:
    """
    Elimina una fórmula en bloque si aparece idéntica al final del
    chunk N y al principio del chunk N+1.
    """
    for i in range(len(chunks) - 1):
        if not chunks[i] or not chunks[i + 1]:
            continue
        ultimo  = chunks[i][-1]
        primero = chunks[i + 1][0]
        if (ultimo.tipo == 'formula'
                and primero.tipo == 'formula'
                and ultimo.texto.strip() == primero.texto.strip()):
            chunks[i + 1].pop(0)
    return chunks
