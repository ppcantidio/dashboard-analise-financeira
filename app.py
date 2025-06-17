import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache
def load_data():
    data = pd.read_csv('data.csv')
    data['data'] = pd.to_datetime(data['data'])
    return data

data = load_data()

# Linha do Tempo de Casos Confirmados por Região
st.title('Linha do Tempo de Casos Confirmados por Região')
for regiao in data['regiao'].unique():
    subset = data[data['regiao'] == regiao]
    plt.figure(figsize=(10, 5))
    plt.plot(subset['data'], subset['casos_confirmados'], marker='o', label=regiao)
    plt.title(f'Casos Confirmados ao Longo do Tempo - {regiao}')
    plt.xlabel('Data')
    plt.ylabel('Casos Confirmados')
    plt.xticks(rotation=45)
    plt.legend()
    st.pyplot(plt)

# Casos Confirmados vs Óbitos (última data disponível)
st.title('Casos Confirmados vs Óbitos (Última Data)')
ultima_data = data['data'].max()
ultima_data_subset = data[data['data'] == ultima_data]
plt.figure(figsize=(10, 5))
plt.bar(ultima_data_subset['regiao'], ultima_data_subset['casos_confirmados'], label='Casos Confirmados', alpha=0.6)
plt.bar(ultima_data_subset['regiao'], ultima_data_subset['obitos'], label='Óbitos', alpha=0.6)
plt.title('Casos Confirmados vs Óbitos')
plt.xlabel('Região')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)
plt.legend()
st.pyplot(plt)

# Letalidade por Região
st.title('Letalidade por Região')
ultima_data_subset['letalidade'] = ultima_data_subset['obitos'] / ultima_data_subset['casos_confirmados'] * 100
plt.figure(figsize=(10, 5))
plt.bar(ultima_data_subset['regiao'], ultima_data_subset['letalidade'], color='red')
plt.title('Letalidade por Região (%)')
plt.xlabel('Região')
plt.ylabel('Letalidade (%)')
st.pyplot(plt)