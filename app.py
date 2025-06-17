import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
@st.cache_data
def load_data():
    data = pd.read_csv('data.csv')
    data['Date'] = pd.to_datetime(data['Date'])
    return data

data = load_data()

# Title
st.title('Dashboard de Análise Financeira')

# Linha de Receita por Empresa
st.subheader('Linha de Receita por Empresa')
for company in data['Company'].unique():
    company_data = data[data['Company'] == company]
    plt.figure(figsize=(10, 5))
    plt.plot(company_data['Date'], company_data['Revenue'], label=company)
    plt.title(f'Receita ao longo do tempo - {company}')
    plt.xlabel('Data')
    plt.ylabel('Receita')
    plt.legend()
    st.pyplot(plt)

# Barras de Receita Total por Região
st.subheader('Barras de Receita Total por Região')
region_revenue = data.groupby('Region')['Revenue'].sum().reset_index()
plt.figure(figsize=(10, 5))
plt.bar(region_revenue['Region'], region_revenue['Revenue'], color='skyblue')
plt.title('Receita Total por Região')
plt.xlabel('Região')
plt.ylabel('Receita')
plt.xticks(rotation=45, ha='right')  # Ajusta os rótulos
st.pyplot(plt)

# Ranking das Top 3 Empresas
st.subheader('Ranking das Top 3 Empresas')
total_revenue = data.groupby('Company')['Revenue'].sum().reset_index().sort_values(by='Revenue', ascending=False).head(3)
plt.figure(figsize=(10, 5))
plt.barh(total_revenue['Company'], total_revenue['Revenue'], color='lightgreen')
plt.title('Ranking das Top 3 Empresas por Receita')
plt.xlabel('Receita')
st.pyplot(plt)
