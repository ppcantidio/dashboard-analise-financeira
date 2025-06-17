import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache
def load_data():
    data = pd.read_csv('data.csv')
    data['data'] = pd.to_datetime(data['data'])
    return data

data = load_data()

st.title('Dashboard COVID-19')

# Linha do Tempo de Casos Confirmados (por Região)
for regiao in data['regiao'].unique():
    regiao_data = data[data['regiao'] == regiao]
    plt.figure(figsize=(10, 5))
    plt.plot(regiao_data['data'], regiao_data['casos_confirmados'], marker='o', label=regiao)
    plt.title(f'Casos Confirmados ao Longo do Tempo - {regiao}')
    plt.xlabel('Data')
    plt.ylabel('Casos Confirmados')
    plt.xticks(rotation=45)
    plt.legend()
    st.pyplot()

# Casos Confirmados vs Óbitos (última data disponível)
ultima_data = data['data'].max()
ultima_data_data = data[data['data'] == ultima_data]
plt.figure(figsize=(10, 5))
plt.bar(ultima_data_data['regiao'], ultima_data_data['casos_confirmados'], label='Casos Confirmados', alpha=0.6)
plt.bar(ultima_data_data['regiao'], ultima_data_data['obitos'], label='Óbitos', alpha=0.6)
plt.title('Casos Confirmados vs Óbitos - Última Data')
plt.xlabel('Região')
plt.ylabel('Quantidade')
plt.legend()
st.pyplot()

# Letalidade por Região
ultima_data_data['letalidade'] = ultima_data_data['obitos'] / ultima_data_data['casos_confirmados'] * 100
plt.figure(figsize=(10, 5))
plt.bar(ultima_data_data['regiao'], ultima_data_data['letalidade'], color='red')
plt.title('Letalidade por Região - Última Data')
plt.xlabel('Região')
plt.ylabel('Letalidade (%)')
st.pyplot()