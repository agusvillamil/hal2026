"""
Intercala problemas de un capítulo con sus soluciones del solucionario.

Uso:
    python intercalar_soluciones.py <capitulo.md> <solucionario.md> [salida.md]

Si se omite salida.md, genera <capitulo>_intercalado.md en el mismo directorio.

El orden del archivo de salida es:
    [contenido anterior al primer ejercicio del capítulo]
    problema 1.1
    solución 1.1   (si existe en el solucionario)
    problema 1.2
    solución 1.2
    ...

Las fórmulas LaTeX se conservan sin modificación.
Si un problema no tiene solución en el solucionario, se incluye sin ella.
"""

import re
import sys
from pathlib import Path

# Patrón que identifica el inicio de un ejercicio: "1.1.", "2.14.", etc.
PATRON_EJERCICIO = re.compile(r'^(\d+\.\d+)\.', re.MULTILINE)


def dividirEnBloques(contenido: str) -> list[tuple[str | None, str]]:
    """
    Divide el contenido en bloques.

    Returns:
        Lista de (id, texto). id es "N.M" para problemas/soluciones,
        None para el contenido previo al primer ejercicio.
    """
    coincidencias = list(PATRON_EJERCICIO.finditer(contenido))

    if not coincidencias:
        return [(None, contenido)]

    bloques = []

    if coincidencias[0].start() > 0:
        bloques.append((None, contenido[:coincidencias[0].start()]))

    for i, m in enumerate(coincidencias):
        fin = coincidencias[i + 1].start() if i + 1 < len(coincidencias) else len(contenido)
        bloques.append((m.group(1), contenido[m.start():fin]))

    return bloques


def parsearSolucionario(contenido: str) -> dict[str, str]:
    """
    Parsea el solucionario y devuelve un dict {id: texto_solución}.
    id tiene formato "N.M" (ej: "1.1", "2.14").
    """
    bloques = dividirEnBloques(contenido)
    return {id_: texto for id_, texto in bloques if id_ is not None}


def intercalar(ruta_capitulo: str, ruta_solucionario: str, ruta_salida: str | None = None) -> None:
    capitulo    = Path(ruta_capitulo)
    solucionario = Path(ruta_solucionario)

    if not capitulo.exists():
        print(f'Error: no se encontró {ruta_capitulo}')
        sys.exit(1)
    if not solucionario.exists():
        print(f'Error: no se encontró {ruta_solucionario}')
        sys.exit(1)

    if ruta_salida is None:
        salida = capitulo.parent / (capitulo.stem + '_intercalado.md')
    else:
        salida = Path(ruta_salida)

    print(f'Capítulo    : {capitulo}')
    print(f'Solucionario: {solucionario}')
    print(f'Salida      : {salida}\n')

    contenido_capitulo    = capitulo.read_text(encoding='utf-8')
    contenido_solucionario = solucionario.read_text(encoding='utf-8')

    bloques_capitulo = dividirEnBloques(contenido_capitulo)
    soluciones       = parsearSolucionario(contenido_solucionario)

    partes          = []
    con_solucion    = 0
    sin_solucion    = 0
    total_problemas = sum(1 for id_, _ in bloques_capitulo if id_ is not None)

    for id_, texto in bloques_capitulo:
        # id_ es None para el contenido previo al primer ejercicio (tablas de
        # conversión, texto introductorio, headers de sección, etc.).
        # Para omitir ese contenido y quedarse solo con problemas y soluciones,
        # reemplazá las dos líneas siguientes por: `if id_ is None: continue`
        partes.append(texto)

        if id_ is None:
            continue

        if id_ in soluciones:
            # Asegurar separación de una línea en blanco entre problema y solución
            if not texto.endswith('\n\n'):
                partes.append('\n')
            partes.append(soluciones[id_])
            con_solucion += 1
        else:
            sin_solucion += 1

    salida.write_text(''.join(partes), encoding='utf-8')

    print(f'Problemas en el capítulo : {total_problemas}')
    print(f'Con solución             : {con_solucion}')
    print(f'Sin solución             : {sin_solucion}')
    print(f'\nArchivo generado: {salida}')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Uso: python intercalar_soluciones.py <capitulo.md> <solucionario.md> [salida.md]')
        sys.exit(1)

    capitulo_arg    = sys.argv[1]
    solucionario_arg = sys.argv[2]
    salida_arg      = sys.argv[3] if len(sys.argv) >= 4 else None

    intercalar(capitulo_arg, solucionario_arg, salida_arg)
