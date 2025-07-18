from PyPDF2 import PdfReader
import os

def extraer_metadatos_pdf(ruta_pdf):
    try:
        reader = PdfReader(ruta_pdf)
        metadatos = reader.metadata
        return {
            'archivo': os.path.basename(ruta_pdf),
            'autor': metadatos.author,
            'software': metadatos.producer,
            'fecha_creacion': metadatos.creation_date,
            'fecha_modificacion': metadatos.modification_date
        }
    except Exception as e:
        return {'error': str(e)}
