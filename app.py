import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    data = pd.read_csv('data.csv')
    return data

def main():
    st.title('Dashboard Financeiro')
    data = load_data()
    st.write(data)

    # Gráficos e análises
    st.subheader('Gráfico de Receita por Empresa')
    revenue_data = data.groupby('Company')['Revenue'].sum().sort_values()
    plt.figure(figsize=(10, 6))
    plt.barh(revenue_data.index, revenue_data.values, color='skyblue')
    plt.xlabel('Receita')
    plt.title('Receita Total por Empresa')
    st.pyplot(plt)

if __name__ == '__main__':
    main()