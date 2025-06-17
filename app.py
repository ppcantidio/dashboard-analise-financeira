import streamlit as st
import pandas as pd

# Carregar os dados
@st.cache_data
def load_data():
    data = pd.read_csv('data.csv')
    return data

data = load_data()

# Título do Dashboard
st.title('Dashboard de Análise Financeira')

# Gráficos e visualizações
st.subheader('Receita por Produto')
product_revenue = data.groupby('Product')['Revenue'].sum().reset_index()
st.bar_chart(product_revenue.set_index('Product'))

st.subheader('Receita por Região')
region_revenue = data.groupby('Region')['Revenue'].sum().reset_index()
st.line_chart(region_revenue.set_index('Region'))

# Tabela com os dados
st.subheader('Dados Originais')
st.dataframe(data)