import streamlit as st

# Colores y estilo
COLOR_FONDO = "#F0F0F3"
COLOR_TEXTO = "#222222"
COLOR_INPUT_BG = "#FFFFFF"
COLOR_INPUT_BORDER = "#CCCCCC"
COLOR_BOTON = "#4FA3C1"
COLOR_BOTON_HOVER = "#3B8A9E"
COLOR_RESULTADO_BG = "#D7F0FA"
COLOR_RESULTADO_FG = "#1A5D73"
COLOR_FOOTER = "#888888"
COLOR_ERROR_BG = "#FFD6D6"
COLOR_ERROR_FG = "#A10000"

st.set_page_config(page_title="Calculadora de Dosis para Animales", page_icon="🐾", layout="centered")

# CSS personalizado
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
        background-color: {COLOR_BOTON_HOVER};
        color: white;
    }}
    input[type="text"] {{
        background-color: {COLOR_INPUT_BG} !important;
        color: {COLOR_TEXTO};
        border: 2px solid {COLOR_INPUT_BORDER};
        border-radius: 5px;
        padding: 8px 10px;
        width: 100%;
        box-sizing: border-box;
        margin-bottom: 10px;
        outline: none !important;
    }}
    input[type="text"]:focus {{
        border: 2px solid {COLOR_BOTON_HOVER} !important;
        box-shadow: none !important;
    }}
    .resultado {{
        background-color: {COLOR_RESULTADO_BG};
        color: {COLOR_RESULTADO_FG};
        padding: 12px;
        border-radius: 5px;
        font-weight: bold;
        text-align: center;
        margin-top: 15px;
    }}
    .error-box {{
        background-color: {COLOR_ERROR_BG};
        color: {COLOR_ERROR_FG};
        padding: 10px;
        border-radius: 5px;
        margin-top: 10px;
        margin-bottom: 10px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Calculadora de Dosis para Animales")

# Inicializar valores en session_state
if "peso" not in st.session_state:
    st.session_state.peso = ""
if "dosis" not in st.session_state:
    st.session_state.dosis = ""
if "conc" not in st.session_state:
    st.session_state.conc = ""
if "resultado" not in st.session_state:
    st.session_state.resultado = ""

# Inputs
st.session_state.peso = st.text_input("Peso del animal (kg):", st.session_state.peso, key="peso_input")
st.session_state.dosis = st.text_input("Dosis (mg/kg):", st.session_state.dosis, key="dosis_input")
st.session_state.conc = st.text_input("Concentración (mg/ml):", st.session_state.conc, key="conc_input")

# Botones
col1, col2 = st.columns(2)

with col1:
    if st.button("Calcular Dosis"):
        errores = []
        try:
            peso = float(st.session_state.peso)
            if peso <= 0:
                errores.append("Peso debe ser mayor que cero.")
        except:
            errores.append("Peso debe ser un número válido.")

        try:
            dosis = float(st.session_state.dosis)
            if dosis <= 0:
                errores.append("Dosis debe ser mayor que cero.")
        except:
            errores.append("Dosis debe ser un número válido.")

        try:
            conc = float(st.session_state.conc)
            if conc <= 0:
                errores.append("Concentración debe ser mayor que cero.")
        except:
            errores.append("Concentración debe ser un número válido.")

        if errores:
            for err in errores:
                st.markdown(f'<div class="error-box">{err}</div>', unsafe_allow_html=True)
        else:
            resultado = (peso * dosis) / conc
            st.session_state.resultado = resultado
            st.markdown(f'<div class="resultado">Debe administrar: {resultado:.2f} ml</div>', unsafe_allow_html=True)
    else:
        # Mostrar resultado si ya se calculó
        if st.session_state.resultado:
            st.markdown(f'<div class="resultado">Debe administrar: {st.session_state.resultado:.2f} ml</div>', unsafe_allow_html=True)

with col2:
    if st.button("Reiniciar"):
        st.session_state.peso = ""
        st.session_state.dosis = ""
        st.session_state.conc = ""
        st.session_state.resultado = None
        st.experimental_rerun()  # Esto recarga la página y limpia todo

# Footer
st.markdown(f"<p style='text-align:right; font-size:10px; color:{COLOR_FOOTER};'>by: R</p>", unsafe_allow_html=True)

