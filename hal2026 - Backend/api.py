from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import ollama

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["*"],
)

class Pregunta(BaseModel):
    mensaje: str

@app.post("/chat")
def chat(pregunta: Pregunta):
    respuesta = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": pregunta.mensaje}]
    )
    return {"respuesta": respuesta["message"]["content"]}
