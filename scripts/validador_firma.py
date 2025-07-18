from scripts.extractor_metadatos import extraer_metadatos_pdf
from scripts.detector_firma_pdfsig import verificar_firma_pdfsig
import joblib
import pandas as pd

def validar_documento(pdf_path, modelo_path):
    meta = extraer_metadatos_pdf(pdf_path)
    firma = verificar_firma_pdfsig(pdf_path)
    fecha_cre = pd.to_datetime(meta['fecha_creacion'], errors='coerce')
    fecha_mod = pd.to_datetime(meta['fecha_modificacion'], errors='coerce')

    features = {
        'FechaDiff': abs((fecha_mod - fecha_cre).days) if pd.notnull(fecha_cre) and pd.notnull(fecha_mod) else 999,
        'Software_Sospechoso': int('acrobat' not in (meta['software'] or '').lower()),
        'FirmaDigital': firma['firma_digital'],
        'TieneTimestamp': firma['timestamp_valido']
    }

    modelo = joblib.load(modelo_path)
    pred = modelo.predict([list(features.values())])[0]
    return {'archivo': meta['archivo'], 'riesgo': pred, 'detalles': features}
