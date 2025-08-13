import streamlit as st

# Colores y estilo
COLOR_FONDO = "#F0F0F3"
COLOR_TEXTO = "#222222"
COLOR_INPUT_BG = "#FFFFFF"
COLOR_BOTON = "#4FA3C1"
COLOR_RESULTADO_BG = "#D7F0FA"
COLOR_RESULTADO_FG = "#1A5D73"
COLOR_FOOTER = "#888888"

st.set_page_config(page_title="Calculadora de Dosis para Animales", page_icon="🐾", layout="centered")

# Fondo personalizado usando CSS
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {COLOR_FONDO};
        color: {COLOR_TEXTO};
        font-family: 'Segoe UI', sans-serif;
    }}
    .stButton>button {{
        background-color: {COLOR_BOTON};
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-weight: bold;
    }}
    .stButton>button:hover {{
        background-color: #3B8A9E;
        color: white;
    }}
    .input-number input {{
        background-color: {COLOR_INPUT_BG};
        color: {COLOR_TEXTO};
        border-radius: 5px;
        padding: 5px 10px;
        width: 100%;
        box-sizing: border-box;
    }}
    .resultado {{
        background-color: {COLOR_RESULTADO_BG};
        color: {COLOR_RESULTADO_FG};
        padding: 10px;
        border-radius: 5px;
        font-weight: bold;
        text-align: center;
        margin-top: 15px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Calculadora de Dosis para Animales")

# Inputs como texto para eliminar botones de más/menos
peso_str = st.text_input("Peso del animal (kg):", "")
dosis_str = st.text_input("Dosis (mg/kg):", "")
conc_str = st.text_input("Concentración (mg/ml):", "")

# Botones
col1, col2 = st.columns(2)

with col1:
    if st.button("Calcular Dosis"):
        errores = []
        try:
            peso = float(peso_str)
            if peso <= 0:
                errores.append("Peso debe ser mayor que cero.")
        except:
            errores.append("Peso debe ser un número válido.")

        try:
            dosis = float(dosis_str)
            if dosis <= 0:
                errores.append("Dosis debe ser mayor que cero.")
        except:
            errores.append("Dosis debe ser un número válido.")

        try:
            conc = float(conc_str)
            if conc <= 0:
                errores.append("Concentración debe ser mayor que cero.")
        except:
            errores.append("Concentración debe ser un número válido.")

        if errores:
            st.error("\n".join(errores))
        else:
            resultado = (peso * dosis) / conc
            st.markdown(f'<div class="resultado">Debe administrar: {resultado:.2f} ml</div>', unsafe_allow_html=True)

with col2:
    if st.button("Reiniciar"):
        st.experimental_rerun()  # Esto reinicia la página entera y limpia los inputs

# Footer
st.markdown(f"<p style='text-align:right; font-size:10px; color:{COLOR_FOOTER};'>by: R</p>", unsafe_allow_html=True)

