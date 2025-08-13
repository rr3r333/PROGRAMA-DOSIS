import streamlit as st

# Colores
COLOR_FONDO = "#F0F0F3"
COLOR_TEXTO = "#222222"
COLOR_INPUT_LABEL = "#000000"  # Letras de los labels en negro
COLOR_INPUT_BG = "#FFFFFF"
COLOR_INPUT_BORDER = "#CCCCCC"
COLOR_INPUT_ERROR_BORDER = "#A10000"
COLOR_BOTON = "#4FA3C1"
COLOR_BOTON_HOVER = "#3B8A9E"
COLOR_RESULTADO_BG = "#D7F0FA"
COLOR_RESULTADO_FG = "#1A5D73"
COLOR_FOOTER = "#888888"
COLOR_ERROR_BG = "#FFD6D6"
COLOR_ERROR_FG = "#A10000"

st.set_page_config(page_title="Calculadora de Dosis para Animales", page_icon="🐾", layout="centered")

# CSS
st.markdown(f"""
<style>
.stApp {{
    background-color: {COLOR_FONDO};
    color: {COLOR_TEXTO};
    font-family: 'Segoe UI', sans-serif;
}}
label {{
    color: {COLOR_INPUT_LABEL} !important;
    font-weight: bold;
    font-size: 16px;
}}
.stButton>button {{
    background-color: {COLOR_BOTON};
    color: white;
    border: none;
    border-radius: 5px;
    font-weight: bold;
    font-size: 14px;
    width: 100%;
    height: 50px;
}}
.stButton>button:hover {{
    background-color: {COLOR_BOTON_HOVER};
}}
input[type="text"] {{
    background-color: {COLOR_INPUT_BG} !important;
    color: #000000; /* Texto dentro del input en negro */
    caret-color: #000000; /* Cursor negro visible */
    border: 2px solid {COLOR_INPUT_BORDER};
    border-radius: 5px;
    padding: 12px 10px;
    width: 100%;
    box-sizing: border-box;
    margin-bottom: 15px;
    font-size: 18px;
    height: 50px;
    outline: none !important;
}}
input[type="text"].error {{
    border: 2px solid {COLOR_INPUT_ERROR_BORDER} !important;
}}
input[type="text"]:focus {{
    border: 2px solid {COLOR_BOTON_HOVER} !important;
    box-shadow: none !important;
}}
.resultado {{
    background-color: {COLOR_RESULTADO_BG};
    color: {COLOR_RESULTADO_FG};
    padding: 14px;
    border-radius: 5px;
    font-weight: bold;
    text-align: center;
    margin-top: 15px;
    font-size: 18px;
}}
.error-box {{
    background-color: {COLOR_ERROR_BG};
    color: {COLOR_ERROR_FG};
    padding: 10px;
    border-radius: 5px;
    margin-top: 10px;
    margin-bottom: 10px;
    font-size: 16px;
}}
</style>
""", unsafe_allow_html=True)

st.title("Calculadora de Dosis para Animales")

# Inicializar session_state
for key in ["peso", "dosis", "conc", "resultado", "errores",
            "peso_input_class", "dosis_input_class", "conc_input_class"]:
    if key not in st.session_state:
        st.session_state[key] = "" if "class" not in key and key != "errores" else []

# Función para calcular
def calcular():
    errores = []
    campos_error = []

    try:
        peso = float(st.session_state.peso)
        if peso <= 0:
            errores.append("Peso debe ser mayor que cero.")
            campos_error.append("peso_input")
    except:
        errores.append("Peso debe ser un número válido.")
        campos_error.append("peso_input")

    try:
        dosis = float(st.session_state.dosis)
        if dosis <= 0:
            errores.append("Dosis debe ser mayor que cero.")
            campos_error.append("dosis_input")
    except:
        errores.append("Dosis debe ser un número válido.")
        campos_error.append("dosis_input")

    try:
        conc = float(st.session_state.conc)
        if conc <= 0:
            errores.append("Concentración debe ser mayor que cero.")
            campos_error.append("conc_input")
    except:
        errores.append("Concentración debe ser un número válido.")
        campos_error.append("conc_input")

    st.session_state.errores = errores
    st.session_state.resultado = "" if errores else (peso * dosis) / conc

    for key in ["peso_input", "dosis_input", "conc_input"]:
        st.session_state[key + "_class"] = "error" if key in campos_error else ""

# Función para reiniciar
def reiniciar():
    for key in ["peso", "dosis", "conc", "resultado", "errores",
                "peso_input_class", "dosis_input_class", "conc_input_class"]:
        st.session_state[key] = "" if "errores" not in key else []
    st.session_state["reiniciado"] = True  # Marcador para JS

# Inputs
st.session_state.peso = st.text_input("Peso del animal (kg):", st.session_state.peso, key="peso_input")
st.session_state.dosis = st.text_input("Dosis (mg/kg):", st.session_state.dosis, key="dosis_input")
st.session_state.conc = st.text_input("Concentración (mg/ml):", st.session_state.conc, key="conc_input")

# Botones
col1, col2 = st.columns(2)
with col1:
    if st.button("Calcular Dosis"):
        calcular()
with col2:
    if st.button("Reiniciar"):
        reiniciar()

# Mostrar errores
if st.session_state.errores:
    for err in st.session_state.errores:
        st.markdown(f'<div class="error-box">{err}</div>', unsafe_allow_html=True)

# Mostrar resultado
if st.session_state.resultado != "":
    st.markdown(f'<div class="resultado">Debe administrar: {st.session_state.resultado:.2f} ml</div>', unsafe_allow_html=True)

# Footer
st.markdown(f"<p style='text-align:right; font-size:10px; color:{COLOR_FOOTER};'>by: R</p>", unsafe_allow_html=True)

# JS para enfocar primer input tras reinicio
if st.session_state.get("reiniciado"):
    st.markdown("""
    <script>
        const firstInput = window.parent.document.querySelector('input[id="peso_input"]');
        if(firstInput){firstInput.focus();}
    </script>
    """, unsafe_allow_html=True)
    st.session_state["reiniciado"] = False
