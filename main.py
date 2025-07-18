from scripts.clasificador_riesgo import entrenar_modelo
from scripts.validador_firma import validar_documento

# 1) Entrenar modelo (solo la primera vez):
entrenar_modelo("datos_entrenamiento.csv", "modelos/clasificador_riesgo.pkl")

# 2) Validar documentos de ejemplo:
for f in ["ejemplos_pdf/firmado_legitimo.pdf", "ejemplos_pdf/firmado_alterado.pdf"]:
    resultado = validar_documento(f, "modelos/clasificador_riesgo.pkl")
    print(f"\n---\nArchivo: {resultado['archivo']}")
    print(f"Riesgo: {resultado['riesgo']}")
    print("Detalles:", resultado['detalles'])

