import streamlit as st

st.title("Minha primeira página")
st.subheader("Feito com Streamlit 👍")

valor1 = st.number_input("Digite o primeiro número", min_value=0.0)
valor2 = st.number_input("Digite o segundo número", min_value=0.0)

if st.button ("calcular"):
    resultado = valor1 = valor2
    st.title(resultado)
    python -m streamlit run app.py 