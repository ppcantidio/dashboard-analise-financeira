import streamlit as st
import pandas as pd

# Carregar os dados
@st.cache
def load_data():
    data = pd.read_csv('data.csv')
    return data

data = load_data()

# Título do Dashboard
st.title('Dashboard de Análise Financeira')

# Gráficos
st.subheader('Receitas, Custos e Lucros ao longo do tempo')
st.line_chart(data[['Date', 'Receitas', 'Custos', 'Lucros']].set_index('Date'))

st.subheader('Fluxo de Caixa ao longo do tempo')
st.line_chart(data[['Date', 'Fluxo_de_Caixa']].set_index('Date'))

# Exibir dados
st.subheader('Dados Financeiros')
st.dataframe(data)