#Funcion que toma una serie de rutas de libros y divide esos 
#libros en chunks de 500 caracteres con un overlap de 100 caracteres 
#y devuelve una lista de chunks

import os
from pathlib import Path
from dotenv import load_dotenv

# Carga el .env desde la raíz del proyecto (un nivel arriba de este archivo)
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

def get_pdf_paths():
    carpeta = Path(os.getenv("PDF_DIR", str(Path(__file__).parent / "Libros")))
    return [str(p) for p in carpeta.glob("*.pdf")]