import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    data = pd.read_csv('data.csv')
    return data

def main():
    st.title('Dashboard Financeiro')
    data = load_data()

    st.subheader('Visão Geral')
    st.write(data)

    st.subheader('Gráficos')
    st.line_chart(data['Revenue'])

if __name__ == '__main__':
    main()