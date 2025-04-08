import streamlit as st
import pandas as pd

st.set_page_config(page_title="Asistente Excel IA")

st.title("📊 Asistente Inteligente para Excel - Autor Sosa Ignacio")
st.write("Cargá tu archivo Excel y hacé preguntas sobre los datos.")

uploaded_file = st.file_uploader("Subí tu archivo Excel", type=["xlsx"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        st.write("Vista previa del archivo:")
        st.dataframe(df)

        pregunta = st.text_input("¿Qué querés saber de este Excel?")

        if pregunta:
            st.write("🔍 Todavía no conectamos IA, pero en breve responderemos esto:")
            st.write(f"👉 {pregunta}")
    except Exception as e:
        st.error(f"Error al leer el archivo: {e}")
