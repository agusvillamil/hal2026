#Funcion que toma una serie de rutas de libros y divide esos
#libros en chunks de 500 caracteres con un overlap de 100 caracteres
#y devuelve una lista de chunks

from conseguirRutas import get_pdf_paths
from docling.document_converter import DocumentConverter
from langchain_text_splitters import RecursiveCharacterTextSplitter

listaDePDF = get_pdf_paths()

_converter = DocumentConverter()

def extraer_texto(ruta):
    """Convierte un PDF a Markdown usando docling.
    Preserva estructura, encabezados y marca fórmulas e imágenes
    que no pueden ser decodificadas como texto."""
    result = _converter.convert(ruta)
    return result.document.export_to_markdown()

def get_chunks(ruta):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    texto = extraer_texto(ruta)
    return splitter.split_text(texto)

if __name__ == "__main__":
    print(listaDePDF[0])  # Imprimir la ruta del primer PDF para verificar
    chunks = get_chunks(listaDePDF[0])  # Procesar solo el primer PDF para el ejemplo
    print(f"Total de chunks generados: {len(chunks)}\n")
    if chunks:
        for i, chunk in enumerate(chunks):  # Mostrar solo los primeros 3 chunks para el ejemplo
            print(f"=== Chunk {i+1} ===")
            print(chunk)
            print(f"\n(longitud: {len(chunk)} caracteres)")
            print("=======================\n")
