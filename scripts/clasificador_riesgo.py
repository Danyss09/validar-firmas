import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

def entrenar_modelo(csv_path, salida_modelo):
    df = pd.read_csv(csv_path)
    X = df.drop(columns=['Clase', 'Archivo'])
    y = df['Clase']
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X, y)
    joblib.dump(modelo, salida_modelo)
    print(f"Modelo guardado en {salida_modelo}")

