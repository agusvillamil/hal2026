#!/usr/bin/env python3
import re
import argparse
from pathlib import Path


PATRON_EJERCICIO = re.compile(
    r"(?m)^#\s*Ejercicio\s+(?P<num>\d+\.\d+)\.?\s*$"
)

PATRONES_SOSPECHOSOS = {
    "posible OCR raro": [
        r"\\Omega",
        r"\\dot\s*\{",
        r"\\scriptstyle\s*\{\s*\\dot",
        r"\\therefore",
        r"\\mathrm\s*\{\s*\{",
        r"[A-Za-z]\s*5\s*\d",
        r"\bi\s*,\s*\\mathrm",
        r"\$i\s",
        r"\$\s*\\dot\s*\{",
    ],

    "posible texto en inglés": [
        r"\bso\b",
        r"\band\b",
        r"\bthe\b",
        r"\bfrom\b",
        r"\bwith\b",
        r"\bwhere\b",
        r"\bwhich\b",
        r"\bthis\b",
        r"\bthat\b",
        r"\btherefore\b",
    ],

    "bloque LaTeX probablemente incompleto": [
        r"\$\$\s*\\begin\{array\}\{l\}\s*\$\$",
        r"\\begin\{array\}\{l\}\s*\$\$",
        r"\$\$\s*\\end\{array\}",
        r"\\begin\{array\}",
        r"\\end\{array\}",
    ],

    "unidades o símbolos sospechosos": [
        r"\\mathrm\s*\{\s*f\s*l\s*\}",
        r"\\mathrm\s*\{\s*k\s*m\s*/\s*m\s*\}",
        r"\\mathrm\s*\{\s*k\s*m\s*/\s*m\s*\^\s*\{\s*3\s*\}\s*\}",
        r"\b3cm\b",
        r"\b3m\b",
        r"\bft>s\b",
    ],

    "posible texto pegado o mal separado": [
        r"[a-záéíóúñ]\)\s*[A-ZÁÉÍÓÚÑ]",
        r"\b[A-Za-z]+N\s*=",
        r"\b[A-Z]\s+[A-Z]⋅",
        r"\bA\s+B⋅",
        r"\bR\s+A\s+B\s+C",
    ],

    "posible ejercicio mezclado": [
        r"pila de oro",
        r"densidad del oro",
        r"valor monetario",
        r"Wagner",
        r"Freya",
    ],

    "encabezado vacío": [
        r"##\s+PLANTEAMIENTO\s*\n\s*\n##\s+EJECUCIÓN",
        r"##\s+IDENTIFICAR\s*\n\s*\n##\s+PLANTEAMIENTO",
        r"##\s+EVALUACIÓN\s*\n\s*(?=# Ejercicio|\Z)",
    ],
}


def obtener_linea(texto: str, indice: int) -> int:
    return texto.count("\n", 0, indice) + 1


def extraer_bloques_por_ejercicio(texto: str) -> list[tuple[str, int, int, str]]:
    """
    Devuelve una lista de bloques:
    (numero_ejercicio, indice_inicio, indice_fin, contenido)
    """
    coincidencias = list(PATRON_EJERCICIO.finditer(texto))
    bloques = []

    for i, match in enumerate(coincidencias):
        numero = match.group("num")
        inicio = match.start()
        fin = coincidencias[i + 1].start() if i + 1 < len(coincidencias) else len(texto)
        contenido = texto[inicio:fin]

        bloques.append((numero, inicio, fin, contenido))

    return bloques


def normalizar_fragmento(fragmento: str, ancho: int = 180) -> str:
    fragmento = re.sub(r"\s+", " ", fragmento).strip()

    if len(fragmento) > ancho:
        fragmento = fragmento[:ancho] + "..."

    return fragmento


def diagnosticar(texto: str) -> list[dict]:
    reportes = []
    bloques = extraer_bloques_por_ejercicio(texto)

    for numero, inicio_bloque, _, contenido in bloques:
        for tipo_error, patrones in PATRONES_SOSPECHOSOS.items():
            for patron in patrones:
                for match in re.finditer(patron, contenido, flags=re.IGNORECASE | re.MULTILINE):
                    inicio_global = inicio_bloque + match.start()
                    linea = obtener_linea(texto, inicio_global)

                    contexto_inicio = max(0, match.start() - 80)
                    contexto_fin = min(len(contenido), match.end() + 80)
                    fragmento = contenido[contexto_inicio:contexto_fin]

                    reportes.append({
                        "ejercicio": numero,
                        "linea": linea,
                        "tipo": tipo_error,
                        "patron": patron,
                        "fragmento": normalizar_fragmento(fragmento),
                    })

    return reportes


def generar_resumen(reportes: list[dict]) -> str:
    conteo_por_tipo = {}
    conteo_por_ejercicio = {}

    for r in reportes:
        conteo_por_tipo[r["tipo"]] = conteo_por_tipo.get(r["tipo"], 0) + 1
        conteo_por_ejercicio[r["ejercicio"]] = conteo_por_ejercicio.get(r["ejercicio"], 0) + 1

    salida = []

    salida.append("Resumen del diagnóstico")
    salida.append("=======================")
    salida.append(f"Total de alertas: {len(reportes)}")
    salida.append("")

    salida.append("Alertas por tipo:")
    for tipo, cantidad in sorted(conteo_por_tipo.items(), key=lambda x: x[1], reverse=True):
        salida.append(f"  {tipo}: {cantidad}")

    salida.append("")
    salida.append("Ejercicios con más alertas:")
    for ejercicio, cantidad in sorted(conteo_por_ejercicio.items(), key=lambda x: x[1], reverse=True)[:15]:
        salida.append(f"  Ejercicio {ejercicio}: {cantidad}")

    return "\n".join(salida)


def main():
    parser = argparse.ArgumentParser(
        description="Diagnostica posibles errores de OCR, traducción o estructura en un archivo Markdown intercalado."
    )

    parser.add_argument(
        "archivo_entrada",
        help="Archivo Markdown intercalado a revisar."
    )

    args = parser.parse_args()

    ruta_entrada = Path(args.archivo_entrada)

    texto = ruta_entrada.read_text(encoding="utf-8")

    reportes = diagnosticar(texto)

    print(generar_resumen(reportes))
    print()


if __name__ == "__main__":
    main()
