from extractor_metadatos import extraer_metadatos_pdf
import joblib
import pandas as pd

def validar_documento(ruta_pdf, ruta_modelo):
    datos = extraer_metadatos_pdf(ruta_pdf)
    fecha_cre = pd.to_datetime(datos['fecha_creacion'])
    fecha_mod = pd.to_datetime(datos['fecha_modificacion'])
    features = {
        'FechaDiff': abs((fecha_mod - fecha_cre).days),
        'Software_Sospechoso': int('acrobat' not in (datos['software'] or '').lower()),
        'Tiene_Timestamp': 0
    }
    modelo = joblib.load(ruta_modelo)
    pred = modelo.predict([list(features.values())])[0]
    return {'archivo': datos['archivo'], 'riesgo': pred, 'detalles': features}

