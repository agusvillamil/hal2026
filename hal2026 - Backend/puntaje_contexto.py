import re
import unicodedata
from typing import Any


STOPWORDS_BUSQUEDA = {
    'acerca', 'actual', 'ahora', 'algo', 'algun', 'alguna', 'algunas', 'alguno',
    'algunos', 'ante', 'antes', 'aquel', 'aquella', 'aquellas', 'aquello',
    'aquellos', 'bien', 'cada', 'como', 'cual', 'cuales', 'cuando', 'cuanto',
    'cuantos', 'dame', 'desambiguar', 'desde', 'donde', 'este', 'esto',
    'estos', 'esta', 'estas', 'explica', 'explicame', 'hacer', 'hace',
    'hacen', 'hasta', 'luego', 'mismo', 'mucho', 'para', 'pero', 'podes',
    'podrias', 'porque', 'pregunta', 'preguntas', 'puede', 'pueden', 'quiero',
    'reciente', 'recientes', 'referencia', 'referencias', 'sobre', 'solo',
    'tambien', 'tengo', 'tiene', 'tienen', 'todo', 'todos', 'trata', 'usar',
    'usuario', 'usuarios',
}

TOKENS_CORTOS_UTILES = {'ley', 'mru', 'mruv', 'mrua', 'mas'}

PALABRAS_FORMULA = {
    'calcular', 'calculo', 'deduce', 'deducir', 'deduccion', 'deriva',
    'derivar', 'ecuacion', 'ecuaciones', 'expresion', 'formula', 'formulas',
    'relacion',
}

PALABRAS_EJERCICIO = {
    'calcula', 'calcular', 'ejemplo', 'ejercicio', 'problema', 'resolucion',
    'resolve', 'resolver', 'solucion',
}

PALABRAS_IMAGEN = {
    'diagrama', 'figura', 'grafica', 'grafico', 'imagen', 'plano', 'tabla',
}

TIPOS_POR_INTENCION = {
    'definicion': {
        'concepto', 'definicion', 'definime', 'define', 'definir', 'explica',
        'explicame', 'que es', 'que significa', 'que son', 'significa',
    },
    'demostracion': {
        'como se deduce', 'deduce', 'deducir', 'deduccion', 'demostra',
        'demostrar', 'demostracion',
    },
    'ejemplo': {'ejemplo', 'aplicacion', 'caso'},
    'ejercicio': {
        'como resolver', 'ejercicio', 'problema', 'resolver', 'resolucion',
        'solucion',
    },
    'teorema': {'teorema', 'ley', 'principio'},
}


def normalizar_texto(texto: Any) -> str:
    texto = str(texto or '').lower()
    texto = unicodedata.normalize('NFKD', texto)
    return ''.join(c for c in texto if not unicodedata.combining(c))


def tokens_relevantes(texto: str) -> set[str]:
    texto = normalizar_texto(texto)
    tokens = set(re.findall(r'[a-z0-9]+', texto))
    return {
        token for token in tokens
        if (
            token not in STOPWORDS_BUSQUEDA
            and (len(token) >= 4 or token in TOKENS_CORTOS_UTILES)
        )
    }


def contar_coincidencias(texto: Any, tokens: set[str]) -> int:
    texto_normalizado = normalizar_texto(texto)
    return sum(1 for token in tokens if token in texto_normalizado)


def detectar_intenciones(pregunta: str) -> set[str]:
    texto = normalizar_texto(pregunta)
    tokens = tokens_relevantes(pregunta)
    intenciones = {
        tipo
        for tipo, pistas in TIPOS_POR_INTENCION.items()
        if pistas.intersection(tokens) or any(pista in texto for pista in pistas)
    }

    if PALABRAS_FORMULA.intersection(tokens):
        intenciones.add('formula')
    if PALABRAS_EJERCICIO.intersection(tokens):
        intenciones.add('ejercicio')
    if PALABRAS_IMAGEN.intersection(tokens):
        intenciones.add('imagen')

    return intenciones


def metadata_bool(meta: dict[str, Any], clave: str) -> bool:
    valor = meta.get(clave)
    if isinstance(valor, bool):
        return valor
    return normalizar_texto(valor) in ('1', 'true', 'si')


def puntaje_metadata(
    meta: dict[str, Any],
    pregunta: str,
    tokens: set[str],
) -> float:
    """
    Suma boosts suaves a la similitud semantica original.

    No usa chequeos exactos como numero_ejercicio o chapter_num: solo senales
    amplias ya guardadas en metadatos, para no sobreajustar la busqueda.
    """
    intenciones = detectar_intenciones(pregunta)
    tipo = normalizar_texto(meta.get('tipo_contenido', ''))

    score = 0.0

    coincidencias_conceptos = contar_coincidencias(meta.get('conceptos', ''), tokens)
    score += min(coincidencias_conceptos * 0.08, 0.32)

    coincidencias_tema = contar_coincidencias(meta.get('topic', ''), tokens)
    score += min(coincidencias_tema * 0.04, 0.12)

    if tipo in intenciones:
        score += 0.18

    if 'formula' in intenciones and metadata_bool(meta, 'tiene_formulas'):
        score += 0.12

    if 'imagen' in intenciones and metadata_bool(meta, 'tiene_imagenes'):
        score += 0.08

    if 'ejercicio' in intenciones and metadata_bool(meta, 'es_ejercicio'):
        score += 0.15

    return score


def rerankear_por_metadata(
    documentos: list[str],
    metadatas: list[dict[str, Any]],
    distancias: list[float],
    pregunta: str,
) -> list[dict[str, Any]]:
    tokens = tokens_relevantes(pregunta)
    candidatos = []

    for indice, (doc, meta) in enumerate(zip(documentos, metadatas)):
        distancia = distancias[indice] if indice < len(distancias) else None
        score_semantico = -distancia if distancia is not None else -indice * 0.001
        score_metadata = puntaje_metadata(meta or {}, pregunta, tokens)

        candidatos.append({
            'documento': doc,
            'metadata': meta or {},
            'distancia': distancia,
            'score': score_semantico + score_metadata,
            'score_metadata': score_metadata,
            'orden_original': indice,
        })

    return sorted(candidatos, key=lambda c: (-c['score'], c['orden_original']))
