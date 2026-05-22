import os
from pathlib import Path
from dotenv import load_dotenv

# Carga el .env desde la raíz del proyecto (un nivel arriba de este archivo)
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

def conseguirRutasPDF():
    carpeta = Path(os.getenv(
        "ZEMANSKY_DIR",
        str(Path(__file__).parent / "Sears-Zemansky" / "Capitulos Completos")
    ))
    return [str(p) for p in carpeta.glob("*.md")]
