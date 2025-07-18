import subprocess

def verificar_firma_pdfsig(pdf_path):
    try:
        resultado = subprocess.run(['pdfsig', pdf_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        salida = resultado.stdout.lower()
        tiene_firma = "signature" in salida and "signed on" in salida
        tiene_timestamp = "timestamp" in salida
        return {
            'firma_digital': int(tiene_firma),
            'timestamp_valido': int(tiene_timestamp)
        }
    except Exception as e:
        return {
            'firma_digital': 0,
            'timestamp_valido': 0,
            'error': str(e)
        }
