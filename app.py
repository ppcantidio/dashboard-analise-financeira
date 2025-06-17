import streamlit as st
import pandas as pd

# Carregar os dados
@st.cache_data
def load_data():
    data = pd.read_csv('data.csv')
    return data

data = load_data()

# Título do Dashboard
st.title('Análise Financeira')

# Gráficos e visualizações
st.subheader('Receita por Empresa')
revenue_chart = data.groupby('Company')['Revenue'].sum().sort_values().plot(kind='barh')
st.pyplot(revenue_chart.figure)

st.subheader('Tabela de Dados')
st.dataframe(data)
