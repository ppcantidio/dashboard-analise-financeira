import streamlit as st
import pandas as pd

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
    revenue_chart = data.groupby('Company')['Revenue'].sum().sort_values().plot(kind='barh')
    st.pyplot(revenue_chart.figure)

if __name__ == '__main__':
    main()