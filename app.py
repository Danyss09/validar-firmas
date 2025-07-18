import streamlit as st
from scripts.validador_firma import validar_documento
import os

st.title("🔍 Validador de Firmas Electrónicas con IA")

archivo_pdf = st.file_uploader("Sube un PDF firmado electrónicamente", type=["pdf"])

if archivo_pdf:
    with open("temporal.pdf", "wb") as f:
        f.write(archivo_pdf.read())

    resultado = validar_documento("temporal.pdf", "modelos/clasificador_riesgo.pkl")
    st.write(f"**Archivo:** {resultado['archivo']}")
    st.write(f"**Riesgo Detectado:** `{resultado['riesgo']}`")
    st.json(resultado['detalles'])
