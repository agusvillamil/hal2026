"""
Traducción de solucionarios en inglés a español preservando fórmulas LaTeX.

Uso:
    python traducir_solucionario.py <archivo.md> [archivo_salida.md]

Si se omite archivo_salida, se genera <archivo>_es.md en el mismo directorio.

El progreso se guarda en <archivo_salida>_progreso.json. Al re-ejecutar,
los bloques ya traducidos se saltean y se retoma desde el último pendiente.
"""

import json
import re
import sys
from pathlib import Path
from modelos import llamarGroq

# Modelo dedicado para traducción: mejor bilingüe y seguimiento de instrucciones.
# Separado del MODELO_GROQ del pipeline para no heredar cambios de configuración.
MODELO_TRADUCCION = 'llama-3.3-70b-versatile'

# Patrón que identifica el inicio de cada ejercicio: "1.1.", "2.14.", etc.
PATRON_EJERCICIO = re.compile(r'^(\d+\.\d+\.)', re.MULTILINE)

# Marcador temporal para fórmulas durante la traducción
MARCA = '⟨F{}⟩'

PROMPT_TRADUCCION = (
    'Eres un traductor técnico de física universitaria. '
    'Traduce el siguiente texto del inglés al español. '
    'Reglas estrictas:\n'
    '- Conserva exactamente los marcadores ⟨F0⟩, ⟨F1⟩, ⟨F2⟩, etc. sin modificarlos.\n'
    '- No traduzcas ni alteres unidades físicas (m, kg, s, N, J, etc.).\n'
    '- Mantén los términos IDENTIFY, SET UP, EXECUTE, EVALUATE en español: '
    'IDENTIFICAR, PLANTEAMIENTO, EJECUCIÓN, EVALUACIÓN.\n'
    '- Devuelve únicamente el texto traducido, sin explicaciones.\n\n'
    'Texto:\n'
)


def extraerFormulas(texto: str) -> tuple[str, list[str]]:
    """
    Reemplaza todas las fórmulas LaTeX con marcadores ⟨F0⟩, ⟨F1⟩, ...

    Orden de extracción: bloques $$ primero (para evitar solapamiento con $),
    luego inline $.

    Returns:
        texto_limpio: texto con marcadores en lugar de fórmulas
        formulas: lista de strings con las fórmulas originales en orden
    """
    formulas = []

    def reemplazar(m: re.Match) -> str:
        idx = len(formulas)
        formulas.append(m.group(0))
        return MARCA.format(idx)

    # Bloques $$...$$ (incluyendo saltos de línea)
    texto = re.sub(r'\$\$[\s\S]*?\$\$', reemplazar, texto)
    # Inline $...$
    texto = re.sub(r'\$[^$\n]+?\$', reemplazar, texto)
    # Entornos \(...\) y \[...\]
    texto = re.sub(r'\\\([\s\S]*?\\\)', reemplazar, texto)
    texto = re.sub(r'\\\[[\s\S]*?\\\]', reemplazar, texto)

    return texto, formulas


def restaurarFormulas(texto: str, formulas: list[str]) -> str:
    """Reemplaza los marcadores ⟨F0⟩, ⟨F1⟩, ... con las fórmulas originales."""
    for idx, formula in enumerate(formulas):
        texto = texto.replace(MARCA.format(idx), formula)
    return texto


def dividirEnBloques(contenido: str) -> list[tuple[str, str]]:
    """
    Divide el contenido en bloques por ejercicio.

    Returns:
        Lista de (id_bloque, texto_bloque). El primer bloque puede ser
        un encabezado sin número (id='header').
    """
    coincidencias = list(PATRON_EJERCICIO.finditer(contenido))

    if not coincidencias:
        return [('header', contenido)]

    bloques = []

    # Texto antes del primer ejercicio (encabezado/título)
    if coincidencias[0].start() > 0:
        bloques.append(('header', contenido[:coincidencias[0].start()]))

    for i, m in enumerate(coincidencias):
        fin = coincidencias[i + 1].start() if i + 1 < len(coincidencias) else len(contenido)
        id_bloque = m.group(1)          # ej: "1.1."
        texto = contenido[m.start():fin]
        bloques.append((id_bloque, texto))

    return bloques


def traducirBloque(texto: str) -> str:
    """
    Traduce un bloque de texto preservando fórmulas LaTeX.

    Extrae fórmulas → traduce texto limpio → restaura fórmulas.
    Los reintentos ante rate limiting los maneja llamarGroq internamente.
    Si agota los reintentos, propaga la excepción para que el llamador
    guarde el progreso y detenga la ejecución.
    """
    texto_limpio, formulas = extraerFormulas(texto)
    mensajes = [{'role': 'user', 'content': PROMPT_TRADUCCION + texto_limpio}]
    traducido = llamarGroq(
        mensajes,
        modelo=MODELO_TRADUCCION,
        max_tokens=2048,
        temperature=0,
    )
    return restaurarFormulas(traducido, formulas)


def cargarProgreso(ruta_progreso: Path) -> dict:
    if ruta_progreso.exists():
        return json.loads(ruta_progreso.read_text(encoding='utf-8'))
    return {}


def guardarProgreso(ruta_progreso: Path, progreso: dict) -> None:
    ruta_progreso.write_text(
        json.dumps(progreso, ensure_ascii=False, indent=2),
        encoding='utf-8',
    )


def ensamblarSalida(bloques: list[tuple[str, str]], progreso: dict) -> str:
    """Une todos los bloques traducidos (o originales si no están en progreso)."""
    partes = []
    for id_bloque, texto_original in bloques:
        partes.append(progreso.get(id_bloque, texto_original))
    return ''.join(partes)


def traducirArchivo(ruta_entrada: str, ruta_salida: str | None = None) -> None:
    entrada = Path(ruta_entrada)
    if not entrada.exists():
        print(f'Error: no se encontró {ruta_entrada}')
        sys.exit(1)

    if ruta_salida is None:
        salida = entrada.parent / (entrada.stem + '_es.md')
    else:
        salida = Path(ruta_salida)

    ruta_progreso = salida.parent / (salida.stem + '_progreso.json')

    print(f'Entrada : {entrada}')
    print(f'Salida  : {salida}')
    print(f'Progreso: {ruta_progreso}\n')

    contenido = entrada.read_text(encoding='utf-8')
    bloques = dividirEnBloques(contenido)
    progreso = cargarProgreso(ruta_progreso)

    pendientes = [(id_b, txt) for id_b, txt in bloques if id_b not in progreso]
    ya_hechos = len(bloques) - len(pendientes)

    print(f'Total de bloques : {len(bloques)}')
    print(f'Ya traducidos    : {ya_hechos}')
    print(f'Pendientes       : {len(pendientes)}\n')

    if not pendientes:
        print('Nada pendiente. Ensamblando salida final...')
    else:
        for i, (id_bloque, texto) in enumerate(pendientes, 1):
            etiqueta = id_bloque if id_bloque != 'header' else 'encabezado'
            print(f'[{ya_hechos + i}/{len(bloques)}] Traduciendo bloque {etiqueta}...')

            try:
                traducido = traducirBloque(texto)
                progreso[id_bloque] = traducido
                guardarProgreso(ruta_progreso, progreso)
            except Exception as e:
                print(f'  Error en bloque {etiqueta}: {e}')
                print('  Progreso guardado. Re-ejecuta el script para continuar.')
                # Ensamblar salida parcial con lo que hay hasta ahora
                salida.write_text(ensamblarSalida(bloques, progreso), encoding='utf-8')
                sys.exit(1)

    salida.write_text(ensamblarSalida(bloques, progreso), encoding='utf-8')
    print(f'\nArchivo traducido guardado en: {salida}')

    if ruta_progreso.exists():
        ruta_progreso.unlink()
        print(f'Archivo de progreso eliminado (traducción completa).')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Uso: python traducir_solucionario.py <archivo.md> [archivo_salida.md]')
        sys.exit(1)

    entrada_arg = sys.argv[1]
    salida_arg  = sys.argv[2] if len(sys.argv) >= 3 else None

    traducirArchivo(entrada_arg, salida_arg)
