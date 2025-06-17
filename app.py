import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
@st.cache
def load_data():
    data = pd.read_csv('data.csv')
    return data

# Função para exibir gráficos
def plot_data(data):
    # Análise por produto
    product_analysis = data.groupby('Product').agg({'UnitsSold': 'sum', 'TotalRevenue': 'sum', 'Profit': 'sum'}).reset_index()
    st.subheader('Análise por Produto')
    st.bar_chart(product_analysis.set_index('Product')[['UnitsSold', 'TotalRevenue', 'Profit']])

    # Comparativo de custos unitários
    cost_comparison = data[['Product', 'CostPerUnit']].drop_duplicates().set_index('Product')
    st.subheader('Comparativo de Custos Unitários')
    st.bar_chart(cost_comparison)

    # Margem de lucro por linha de produto
    data['ProfitMargin'] = data['Profit'] / data['TotalRevenue']
    profit_margin = data.groupby('Product')['ProfitMargin'].mean().reset_index()
    st.subheader('Margem de Lucro por Linha de Produto')
    st.bar_chart(profit_margin.set_index('Product'))

    # Distribuição de vendas por região
    sales_by_region = data.groupby('Region')['TotalRevenue'].sum().reset_index()
    st.subheader('Distribuição de Vendas por Região')
    st.bar_chart(sales_by_region.set_index('Region'))

    # Tendências de preço e volume ao longo do tempo
    data['Date'] = pd.to_datetime(data['Date'])
    trend_data = data.groupby('Date').agg({'UnitsSold': 'sum', 'UnitPrice': 'mean'}).reset_index()
    st.subheader('Tendências de Preço e Volume ao Longo do Tempo')
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(trend_data['Date'], trend_data['UnitsSold'], 'g-')
    ax2.plot(trend_data['Date'], trend_data['UnitPrice'], 'b-')
    ax1.set_xlabel('Data')
    ax1.set_ylabel('Unidades Vendidas', color='g')
    ax2.set_ylabel('Preço Médio', color='b')
    st.pyplot(fig)

# Executar o aplicativo
if __name__ == '__main__':
    st.title('Dashboard de Análise de Vendas')
    data = load_data()
    plot_data(data)
