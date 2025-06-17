import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache
def load_data():
    data = pd.read_csv('data.csv')
    return data

def plot_units_revenue_profit(data):
    fig, ax = plt.subplots(3, 1, figsize=(10, 15))
    data.groupby('Product').agg({'UnitsSold': 'sum', 'TotalRevenue': 'sum', 'Profit': 'sum'}).plot(kind='bar', ax=ax[0])
    ax[0].set_title('Unidades Vendidas, Receita e Lucro por Produto')
    ax[0].set_ylabel('Total')

    data.groupby('Product')['CostPerUnit'].mean().plot(kind='bar', ax=ax[1])
    ax[1].set_title('Comparativo de Custos Unitários')
    ax[1].set_ylabel('Custo Médio por Unidade')

    data.groupby('Product').agg({'Profit': 'sum'}).plot(kind='bar', ax=ax[2])
    ax[2].set_title('Margem de Lucro por Linha de Produto')
    ax[2].set_ylabel('Lucro Total')

    plt.tight_layout()
    st.pyplot(fig)

def plot_sales_distribution(data):
    sales_distribution = data.groupby('Region')['TotalRevenue'].sum().sort_values()
    sales_distribution.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Distribuição de Vendas por Região')
    plt.ylabel('')
    st.pyplot()

def main():
    st.title('Dashboard de Análise Financeira')
    data = load_data()
    plot_units_revenue_profit(data)
    plot_sales_distribution(data)

if __name__ == '__main__':
    main()