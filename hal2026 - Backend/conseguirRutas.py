import os
from pathlib import Path
from dotenv import load_dotenv

# Carga el .env desde la raíz del proyecto (un nivel arriba de este archivo)
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

def conseguirRutasPDF():
    carpeta = Path(os.getenv("PDF_DIR", str(Path(__file__).parent / "Libros/Libros_Markdown")))
    return [str(p) for p in carpeta.glob("*.md")]
