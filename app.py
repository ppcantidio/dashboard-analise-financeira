import streamlit as st
import pandas as pd

# Load data
@st.cache_data
def load_data():
    data = pd.read_csv('data.csv')
    return data

data = load_data()

# Title
st.title('Dashboard de Análise Financeira')

# Display data
st.subheader('Dados de Receita')
st.write(data)

# Visualizations
st.subheader('Receita por Empresa')
st.bar_chart(data.groupby('Company')['Revenue'].sum())

# Visualização por Região
st.subheader('Receita por Região')
st.bar_chart(data.groupby('Region')['Revenue'].sum())
