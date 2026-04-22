# HAL 2026 — Asistente de Física I

Asistente conversacional para la materia Física I (UNS), con soporte para fórmulas LaTeX y consultas sobre el material bibliográfico del curso. Las respuestas se generan mediante un pipeline RAG (*Retrieval-Augmented Generation*) que busca contexto relevante en la bibliografía indexada antes de responder.

hal2026.dev.ar

## Estructura del proyecto

```
hal2026/
├── app/                          # Rutas de Next.js
├── components/                   # Componentes React
├── hal2026 - Backend/            # API Python (FastAPI + RAG)
│   ├── api.py                    # Servidor FastAPI — endpoint POST /chat
│   ├── chunking.py               # Orquestador del pipeline de chunking
│   ├── tokenizacion.py           # Fase 1: tokenización en bloques atómicos
│   ├── agrupacion.py             # Fase 2: agrupación greedy por tamaño
│   ├── procesado.py              # Fase 3: correcciones estructurales
│   ├── superposicion.py          # Fase 4: overlap configurable entre chunks
│   ├── enriquecimiento.py        # Descripción de imágenes con Groq vision
│   ├── indexado.py               # Indexado en ChromaDB con metadatos
│   ├── conseguirRutas.py         # Descubrimiento de archivos Markdown
│   ├── requirements.txt          # Dependencias Python
│   └── Libros/                   # Bibliografía (no incluida en el repo)
│       ├── Libros_Markdown/      # Markdown generado por MinerU
│       └── Libros_Chunks/        # Chunks exportados como .txt
├── .env.example                  # Plantilla de variables de entorno
└── README.md
```

---

## Cómo funciona el backend

### Consulta via API (`POST /chat`)

Cuando el frontend envía una pregunta, el backend realiza los siguientes pasos:

```
Usuario: "¿Qué es la fuerza de rozamiento?"
         │
         ▼
1. ChromaDB — embedding local (all-MiniLM-L6-v2)
   Busca los 5 chunks más similares por coseno
         │
         ▼
2. Construcción del contexto
   Cada chunk se etiqueta con su fuente (tema + rango de páginas)
         │
         ▼
3. Groq — llama-3.3-70b-versatile
   Recibe: prompt de sistema + contexto + pregunta
   Responde: solo con información del contexto, en español, con LaTeX
         │
         ▼
{"respuesta": "La fuerza de rozamiento es..."}
```

### Indexado de la bibliografía (`indexado.py`)

Antes de poder responder consultas, los archivos Markdown deben ser procesados e indexados. El proceso es incremental: si un archivo ya fue indexado en una ejecución anterior, se omite sin hacer llamadas a la API.

```
conseguirRutasPDF()
  Descubre todos los .md en Libros/Libros_Markdown/
         │
         ▼
chunkear(ruta)  ←── por cada archivo
  │
  ├─ tokenizar()              — divide en bloques: header / formula / image / text
  ├─ agruparEnChunks()        — agrupa hasta ~1500 caracteres respetando oraciones
  ├─ arreglarEncabezadosSolos()  — mueve headers huérfanos al chunk siguiente
  ├─ arreglarContextoImagenes()  — arrastra texto descriptivo junto a imágenes
  ├─ deduplicarFormulas()     — elimina fórmulas repetidas en fronteras de chunks
  ├─ aplicarSuperposicion()   — agrega 15% del chunk anterior como contexto
  ├─ enriquecerChunk()        — describe imágenes con Groq vision (llama-4-scout)
  └─ guardarChunks()          — guarda .txt en Libros_Chunks/ (solo si no existe)
         │
         ▼
indexarTodos()  ←── por cada archivo
  ├─ Chequeo incremental: ¿file_id ya existe en ChromaDB? → saltar
  ├─ extraerMetadatosArchivo()  — parsea nombre MinerU → capítulo, tema, páginas
  ├─ detectar has_formulas / has_images desde el texto (regex, sin API)
  ├─ extraerMetadatosGroq()     — clasifica tipo de contenido y conceptos físicos
  └─ coleccion.add()            — genera embedding local y persiste en ChromaDB
```

---

## Requisitos previos

- [Node.js](https://nodejs.org/) v18+
- [Python](https://www.python.org/) 3.10+
- [ngrok](https://ngrok.com/) para exponer la API
- Clave de API de [Groq](https://console.groq.com/) (`GROQ_API_KEY`)

---

## Configuración inicial

### 1. Variables de entorno

```bash
cp .env.example .env
```

Completá `.env` con tus valores:

```env
NEXT_PUBLIC_API_URL=https://tu-subdominio.ngrok-free.app
PDF_DIR=./Libros
GROQ_API_KEY=tu_clave_api_groq_aqui
```

### 2. Archivos Markdown

Colocá los archivos `.md` generados por MinerU en:

```
hal2026 - Backend/Libros/Libros_Markdown/
```

Los archivos deben seguir el patrón de nombre:
`MinerU_markdown_Ochoa-{num}-{tema}-{inicio}-{fin}_{id}.md`

---

## Levantar el sistema localmente

### Backend (FastAPI)

```bash
cd "hal2026 - Backend"

# Crear entorno virtual (solo la primera vez)
python -m venv venv

# Activar entorno virtual
source venv/bin/activate        # Linux / macOS
# venv\Scripts\activate         # Windows

# Instalar dependencias (solo la primera vez)
pip install -r requirements.txt

# Indexar la bibliografía (solo la primera vez, o al agregar archivos nuevos)
python indexado.py

# Iniciar el servidor
uvicorn api:app --reload --port 8000
```

La API queda disponible en [http://localhost:8000](http://localhost:8000).

> El indexado puede tardar varios minutos la primera vez, ya que procesa cada archivo con Groq para describir imágenes y extraer metadatos semánticos. Las ejecuciones siguientes omiten archivos ya indexados.

### Frontend (Next.js)

```bash
npm install
npm run dev
```

La app queda disponible en [http://localhost:3000](http://localhost:3000).

### Exponer la API con ngrok

Con la API corriendo, en otra terminal:

```bash
ngrok http 8000
```

Copiá la URL pública (`https://xxxx.ngrok-free.app`) y actualizá `NEXT_PUBLIC_API_URL` en `.env`.

> Cada vez que reiniciás ngrok se genera una URL nueva. Actualizá `.env` y reiniciá el servidor de Next.js.

---

## Orden de inicio recomendado

1. `python indexado.py` — indexar bibliografía (solo si hay archivos nuevos)
2. `uvicorn api:app --reload` — API FastAPI (desde `hal2026 - Backend/`)
3. `ngrok http 8000` — túnel público, actualizar `.env` con la nueva URL
4. `npm run dev` — frontend Next.js
