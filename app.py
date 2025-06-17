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

# Séries Temporais por Empresa
st.subheader('Séries Temporais por Empresa')
for company in data['Company'].unique():
    company_data = data[data['Company'] == company]
    company_data.set_index('Date', inplace=True)
    company_data['Revenue_MA'] = company_data['Revenue'].rolling(window=14).mean()
    plt.figure(figsize=(10, 5))
    plt.plot(company_data.index, company_data['Revenue'], label='Receita', color='blue')
    plt.plot(company_data.index, company_data['Revenue_MA'], label='Média Móvel (14 dias)', color='orange')
    plt.title(f'Receita ao longo do tempo - {company}')
    plt.xlabel('Data')
    plt.ylabel('Receita')
    plt.legend()
    st.pyplot(plt)

# Comparativo de Receita por Região
st.subheader('Comparativo de Receita por Região')
monthly_revenue_region = data.resample('M', on='Date').sum().groupby('Region')['Revenue'].sum().reset_index()
plt.figure(figsize=(10, 5))
plt.bar(monthly_revenue_region['Region'], monthly_revenue_region['Revenue'], color='skyblue')
plt.title('Receita Total por Região')
plt.xlabel('Região')
plt.ylabel('Receita')
st.pyplot(plt)

# Ranking das Top Empresas
st.subheader('Ranking das Top Empresas')
total_revenue = data.groupby('Company')['Revenue'].sum().reset_index().sort_values(by='Revenue', ascending=False)
plt.figure(figsize=(10, 5))
plt.barh(total_revenue['Company'], total_revenue['Revenue'], color='lightgreen')
plt.title('Ranking das Top Empresas por Receita')
plt.xlabel('Receita')
st.pyplot(plt)

# Evolução Mensal de Market Share
st.subheader('Evolução Mensal de Market Share')
monthly_share = data.groupby(['Date', 'Company'])['Revenue'].sum().unstack().fillna(0)
monthly_share = monthly_share.div(monthly_share.sum(axis=1), axis=0)
plt.figure(figsize=(10, 5))
monthly_share.plot.area(stacked=True)
plt.title('Evolução Mensal de Market Share')
plt.xlabel('Data')
plt.ylabel('Participação Percentual')
st.pyplot(plt)

# Mapa de Calor de Dias x Receita
st.subheader('Mapa de Calor de Dias x Receita')
data['Month'] = data['Date'].dt.to_period('M')
heatmap_data = data.pivot_table(index=data['Date'].dt.day, columns='Month', values='Revenue', aggfunc='sum')
plt.figure(figsize=(12, 6))
sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt='.0f')
plt.title('Mapa de Calor de Dias x Receita')
plt.xlabel('Mês')
plt.ylabel('Dia do Mês')
st.pyplot(plt)

# Crescimento Percentual Mês-a-Mês
st.subheader('Crescimento Percentual Mês-a-Mês')
monthly_growth = data.resample('M', on='Date').sum()['Revenue'].pct_change() * 100
plt.figure(figsize=(10, 5))
plt.bar(monthly_growth.index, monthly_growth, color='purple')
plt.title('Crescimento Percentual Mês-a-Mês')
plt.xlabel('Mês')
plt.ylabel('Crescimento Percentual (%)')
st.pyplot(plt)

# Boxplot de Receita por Região
st.subheader('Boxplot de Receita por Região')
sns.boxplot(x='Region', y='Revenue', data=data)
plt.title('Distribuição da Receita por Região')
st.pyplot(plt)

# Gráfico de Dispersão (Revenue vs. Tempo)
st.subheader('Gráfico de Dispersão (Revenue vs. Tempo)')
sns.scatterplot(x='Date', y='Revenue', hue='Company', data=data)
plt.title('Dispersão de Receita ao Longo do Tempo')
st.pyplot(plt)

# Tabela Dinâmica/Resumo Estatístico
st.subheader('Resumo Estatístico de Receita')
st.write(data.groupby(['Company', 'Region'])['Revenue'].agg(['sum', 'mean', 'min', 'max', 'count']))

# Gráfico de Tendência com Linha de Tendência Linear
st.subheader('Gráfico de Tendência com Linha de Tendência Linear')
for company in data['Company'].unique():
    company_data = data[data['Company'] == company]
    sns.regplot(x='Date', y='Revenue', data=company_data, label=company)
plt.title('Tendência de Receita por Empresa')
plt.xlabel('Data')
plt.ylabel('Receita')
st.pyplot(plt)

# Visão de Crescimento Acumulado
st.subheader('Visão de Crescimento Acumulado')
data['Crescimento_Acumulado'] = data.groupby('Company')['Revenue'].cumsum()
for company in data['Company'].unique():
    company_data = data[data['Company'] == company]
    plt.plot(company_data['Date'], company_data['Crescimento_Acumulado'], label=company)
plt.title('Crescimento Acumulado por Empresa')
plt.xlabel('Data')
plt.ylabel('Crescimento Acumulado')
plt.legend()
st.pyplot(plt)

# Análise de Correlação
st.subheader('Análise de Correlação')
correlation_matrix = data.pivot_table(index='Date', columns='Company', values='Revenue', aggfunc='sum').corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlação entre Receitas')
st.pyplot(plt)
