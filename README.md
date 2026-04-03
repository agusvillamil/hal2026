# HAL 2026 — Asistente de Física I

Asistente conversacional para la materia Física I (UNS), con soporte para fórmulas LaTeX y consultas sobre el material bibliográfico del curso.

## Estructura del proyecto

```
hal2026/
├── app/                        # Rutas de Next.js
├── components/                 # Componentes React
├── hal2026 - Backend/          # API Python (FastAPI + Ollama)
│   ├── api.py                  # Servidor FastAPI
│   ├── chunking.py             # Procesamiento de PDFs
│   ├── conseguirRutas.py       # Lectura de rutas de PDFs
│   ├── requirements.txt        # Dependencias Python
│   └── Libros/                 # PDFs de la bibliografía
├── .env.example                # Plantilla de variables de entorno
└── README.md
```

## Requisitos previos

- [Node.js](https://nodejs.org/) v18+
- [Python](https://www.python.org/) 3.10+
- [Ollama](https://ollama.com/) instalado localmente
- [ngrok](https://ngrok.com/) para exponer la API

---

## Configuración inicial

### 1. Variables de entorno

Copiá el archivo de ejemplo y completá los valores:

```bash
cp .env.example .env
```

Editá `.env` con la URL de ngrok activa (ver sección ngrok más abajo):

```env
NEXT_PUBLIC_API_URL=https://tu-subdominio.ngrok-free.app
PDF_DIR=./Libros
```

---

## Levantar el frontend (Next.js)

```bash
# Instalar dependencias
npm install

# Modo desarrollo
npm run dev
```

La app queda disponible en [http://localhost:3000](http://localhost:3000).

---

## Levantar la API Python (FastAPI)

```bash
cd "hal2026 - Backend"

# Crear entorno virtual (solo la primera vez)
python -m venv venv

# Activar entorno virtual
source venv/bin/activate        # Linux / macOS
# venv\Scripts\activate         # Windows

# Instalar dependencias (solo la primera vez)
pip install -r requirements.txt

# Iniciar el servidor
uvicorn api:app --reload --port 8000
```

La API queda disponible en [http://localhost:8000](http://localhost:8000).

---

## Exponer la API con ngrok

Con la API corriendo en el paso anterior, en otra terminal:

```bash
ngrok http 8000
```

ngrok mostrará una URL pública del tipo `https://xxxx.ngrok-free.app`.
Copiá esa URL y actualizá `NEXT_PUBLIC_API_URL` en `.env`.

> Cada vez que reiniciás ngrok se genera una URL nueva. Actualizá `.env` y reiniciá el servidor de Next.js.

---

## Levantar Ollama

Ollama debe estar corriendo para que la API pueda generar respuestas:

```bash
# Iniciar el servidor de Ollama
ollama serve

# Descargar el modelo (solo la primera vez)
ollama pull mistral
```

Ollama corre en [http://localhost:11434](http://localhost:11434) por defecto.

---

## Orden de inicio recomendado

1. `ollama serve` — modelo de lenguaje
2. `uvicorn api:app --reload` — API FastAPI (desde `hal2026 - Backend/`)
3. `ngrok http 8000` — túnel público, actualizar `.env` con la nueva URL
4. `npm run dev` — frontend Next.js
