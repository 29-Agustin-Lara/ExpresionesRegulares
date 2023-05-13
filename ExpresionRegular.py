import streamlit as st
import pandas as pd

st.set_page_config(page_title='Expresiones regulares con datos de Excel', page_icon=':guardsman:', layout='wide')

st.title('Expresiones regulares con datos de Excel')
st.title('Agustin Lara Jimenez - 201229')

df = pd.read_excel("contactos_2023.xlsx")

nombre = st.text_input("Buscar por nombre")

df['Nombre Contacto'] = df['Nombre Contacto'].str.upper()

filtered_df = df[df['Nombre Contacto'].str.contains(nombre.upper(), regex=True, na=False)]

st.write(filtered_df)

