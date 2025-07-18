from scripts.clasificador_riesgo import entrenar_modelo
entrenar_modelo("datos_entrenamiento.csv", "modelos/clasificador_riesgo.pkl")
print("Modelo entrenado y guardado correctamente.")
