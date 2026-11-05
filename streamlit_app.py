import random

import streamlit as st

FRASES = [
    "Hecho es mejor que perfecto.",
    "Primero que funcione, después que sea lindo.",
    "Si compila, es hora de un mate.",
    "Todo bug es una feature que todavía no encontró su público.",
    "Un commit chico por día mantiene lejos al merge conflict.",
]

st.title("🎈 Frase del día")
st.write("Tocá el botón y llevate una frase para arrancar.")

if st.button("Dame una frase"):
    st.success(random.choice(FRASES))
    st.balloons()
