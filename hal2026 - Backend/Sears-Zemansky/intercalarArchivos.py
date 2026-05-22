#!/usr/bin/env python3
import re
import argparse
from pathlib import Path


PATRON_PROBLEMA = re.compile(
    r"(?m)^(?P<num>\d+\.\d+)\.\s+"
)

PATRON_SOLUCION = re.compile(
    r"(?m)^#\s*Ejercicio\s+(?P<num>\d+\.\d+)\.?\s*$"
)

PATRON_TITULOS_SECCION = re.compile(
    r"(?m)^#\s*(Ejercicios|Problemas|Problemas de desafío|Sección\s+.+)\s*$"
)


def eliminar_titulos_seccion(texto: str) -> str:
    """
    Elimina títulos estructurales del archivo de problemas, por ejemplo:

    # Ejercicios
    # Problemas
    # Problemas de desafío
    # Sección 1.8 Componentes de vectores

    No elimina encabezados de soluciones tipo:
    # Ejercicio 1.1
    """
    return PATRON_TITULOS_SECCION.sub("", texto)


def limpiar_espacios(texto: str) -> str:
    """
    Limpia excesos de líneas en blanco sin modificar el contenido textual.
    """
    texto = re.sub(r"\n{3,}", "\n\n", texto)
    return texto.strip()


def extraer_bloques_problemas(texto: str) -> dict[str, str]:
    """
    Extrae bloques del archivo de problemas.

    Convierte cada bloque de:

    1.1. Texto del problema...

    a:

    # Ejercicio 1.1
    Texto del problema...
    """
    texto = eliminar_titulos_seccion(texto)
    coincidencias = list(PATRON_PROBLEMA.finditer(texto))
    bloques = {}

    for i, match in enumerate(coincidencias):
        numero = match.group("num")
        inicio_contenido = match.end()
        fin = coincidencias[i + 1].start() if i + 1 < len(coincidencias) else len(texto)

        contenido_problema = texto[inicio_contenido:fin]
        contenido_problema = eliminar_titulos_seccion(contenido_problema)
        contenido_problema = limpiar_espacios(contenido_problema)

        bloque = f"# Ejercicio {numero}\n{contenido_problema}"
        bloques[numero] = bloque

    return bloques


def extraer_bloques_soluciones(texto: str) -> dict[str, str]:
    """
    Extrae bloques del archivo de soluciones.

    Cada bloque empieza con:
    # Ejercicio 1.1

    Ese encabezado se elimina porque el archivo final ya lo genera
    a partir del problema.
    """
    coincidencias = list(PATRON_SOLUCION.finditer(texto))
    bloques = {}

    for i, match in enumerate(coincidencias):
        numero = match.group("num")
        inicio = match.end()
        fin = coincidencias[i + 1].start() if i + 1 < len(coincidencias) else len(texto)

        bloque = texto[inicio:fin]
        bloque = eliminar_titulos_seccion(bloque)
        bloque = limpiar_espacios(bloque)

        bloques[numero] = bloque

    return bloques


def intercalar(problemas: dict[str, str], soluciones: dict[str, str]) -> str:
    """
    Intercala cada problema con su solución.

    Formato final:

    # Ejercicio 1.1
    Enunciado...

    ## IDENTIFICAR
    ...
    """
    salida = []

    for numero, bloque_problema in problemas.items():
        salida.append(bloque_problema)

        if numero in soluciones:
            salida.append(soluciones[numero])

    resultado = "\n\n".join(salida)
    resultado = eliminar_titulos_seccion(resultado)
    resultado = limpiar_espacios(resultado)

    return resultado + "\n"


def revisar_resultado(texto: str) -> list[str]:
    """
    Hace controles simples sobre el archivo generado.
    """
    advertencias = []

    titulos_restantes = PATRON_TITULOS_SECCION.findall(texto)
    if titulos_restantes:
        advertencias.append("Todavía quedaron títulos de sección en el archivo generado.")

    ejercicios = re.findall(r"(?m)^# Ejercicio\s+(\d+\.\d+)\.?\s*$", texto)
    repetidos = sorted({num for num in ejercicios if ejercicios.count(num) > 1})

    if repetidos:
        advertencias.append(
            "Hay ejercicios repetidos en la salida: " + ", ".join(repetidos)
        )

    return advertencias


def main():
    parser = argparse.ArgumentParser(
        description="Intercala problemas de física con sus soluciones correspondientes."
    )

    parser.add_argument(
        "archivo_problemas",
        help="Ruta del archivo Markdown que contiene los problemas."
    )

    parser.add_argument(
        "archivo_soluciones",
        help="Ruta del archivo Markdown que contiene las soluciones."
    )

    parser.add_argument(
        "archivo_salida",
        help="Ruta del archivo Markdown de salida."
    )

    args = parser.parse_args()

    ruta_problemas = Path(args.archivo_problemas)
    ruta_soluciones = Path(args.archivo_soluciones)
    ruta_salida = Path(args.archivo_salida)

    texto_problemas = ruta_problemas.read_text(encoding="utf-8")
    texto_soluciones = ruta_soluciones.read_text(encoding="utf-8")

    problemas = extraer_bloques_problemas(texto_problemas)
    soluciones = extraer_bloques_soluciones(texto_soluciones)

    resultado = intercalar(problemas, soluciones)

    ruta_salida.write_text(resultado, encoding="utf-8")

    problemas_sin_solucion = set(problemas) - set(soluciones)
    soluciones_sin_problema = set(soluciones) - set(problemas)

    if problemas_sin_solucion:
        print("Problemas sin solución encontrada:")
        for numero in sorted(problemas_sin_solucion):
            print(f"  {numero}")

    if soluciones_sin_problema:
        print("Soluciones sin problema correspondiente:")
        for numero in sorted(soluciones_sin_problema):
            print(f"  {numero}")

    advertencias = revisar_resultado(resultado)

    if advertencias:
        print("\nAdvertencias:")
        for advertencia in advertencias:
            print(f"  {advertencia}")


if __name__ == "__main__":
    main()
