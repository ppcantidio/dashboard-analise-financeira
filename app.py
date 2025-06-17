import streamlit as st
import pandas as pd

# Carregar os dados
@st.cache_data
def load_data():
    data = pd.read_csv('data.csv')
    return data

data = load_data()

# Título do dashboard
st.title('Análise Financeira')

# Gráficos e visualizações
st.subheader('Receita por Região')
revenue_by_region = data.groupby('Region')['Revenue'].sum().reset_index()
st.bar_chart(revenue_by_region.set_index('Region'))

st.subheader('Tabela de Dados')
st.dataframe(data)