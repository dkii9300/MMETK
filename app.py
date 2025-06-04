
import streamlit as st
from modules.models import ENGINE_DATA
from modules.calculations import calculate_clo_mcr, calculate_sfoc, calculate_eexi
from modules.formulas import FORMULAS
from modules.localization import TRANSLATIONS

st.set_page_config(page_title="Marine Main Engine Toolkit", layout="wide")

# Язык по умолчанию
lang = st.sidebar.selectbox("Language / ენა", ["en", "ka"])
t = TRANSLATIONS[lang]

st.title(t["title"])
st.sidebar.text("Marine Main Engine Toolkit by Dimitri K.")

# Выбор модели двигателя
engine_model = st.selectbox(t["select_engine"], list(ENGINE_DATA.keys()))
engine = ENGINE_DATA[engine_model]

# Отображение формулы и расчёт CLO
st.subheader(t["clo_calc"])
st.latex(FORMULAS["CLO_MCR"])

clo_result = calculate_clo_mcr(engine["MCR"], engine["CLO_per_cyl"], engine["cylinders"])
st.markdown(f"**CLO Total [L/h]:** `{clo_result:.2f}`")

# Блок SFOC
st.subheader("SFOC Calculation")
st.latex(FORMULAS["SFOC"])

fuel_kg = st.number_input("Fuel consumed [kg]", value=1000)
power_kw = st.number_input("Output Power [kW]", value=engine["MCR"])
hours = st.number_input("Time [h]", value=1)

sfoc_val = calculate_sfoc(fuel_kg, power_kw, hours)
st.markdown(f"**SFOC [g/kWh]:** `{sfoc_val:.2f}`")

# Блок EEXI
st.subheader(t["eexi_calc"])
st.latex(FORMULAS["EEXI"])

dwt = st.number_input("Deadweight [t]", value=50000)
vref = st.number_input("Reference Speed [knots]", value=13)

eexi_val = calculate_eexi(engine["MCR"], sfoc_val, dwt, vref)
st.markdown(f"**EEXI [gCO2/t·nm]:** `{eexi_val:.3f}`")
