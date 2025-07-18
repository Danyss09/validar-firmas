from PyPDF2 import PdfReader
import os

def extraer_metadatos_pdf(ruta_pdf):
    reader = PdfReader(ruta_pdf)
    meta = reader.metadata
    return {
        'archivo': os.path.basename(ruta_pdf),
        'autor': meta.author,
        'software': meta.producer,
        'fecha_creacion': meta.creation_date,
        'fecha_modificacion': meta.modification_date
    }

