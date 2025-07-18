import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

def entrenar_modelo(csv_path, modelo_path):
    df = pd.read_csv(csv_path)
    X = df.drop(columns=['Archivo', 'Clase'])
    y = df['Clase']
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X, y)
    joblib.dump(modelo, modelo_path)
