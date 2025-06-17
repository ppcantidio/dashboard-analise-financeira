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
st.subheader('Dados')
st.write(data)

# Revenue by Company
st.subheader('Receita por Empresa')
revenue_by_company = data.groupby('Company')['Revenue'].sum().reset_index()
st.bar_chart(revenue_by_company.set_index('Company'))

# Revenue by Region
st.subheader('Receita por Região')
revenue_by_region = data.groupby('Region')['Revenue'].sum().reset_index()
st.bar_chart(revenue_by_region.set_index('Region'))
