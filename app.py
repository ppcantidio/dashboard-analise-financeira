import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    data = pd.read_csv('data.csv')
    return data

data = load_data()

st.title('Dashboard de Análise Financeira')

# Gráficos e visualizações
st.subheader('Receita por Produto')
revenue_by_product = data.groupby('Product')['Revenue'].sum().reset_index()
st.bar_chart(revenue_by_product.set_index('Product'))

st.subheader('Receita por Região')
revenue_by_region = data.groupby('Region')['Revenue'].sum().reset_index()
st.line_chart(revenue_by_region.set_index('Region'))

st.subheader('Tabela de Dados')
st.dataframe(data)