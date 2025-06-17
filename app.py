import streamlit as st
import pandas as pd
import plotly.graph_objects as go

@st.cache

def load_data():
    data = pd.read_csv('data.csv')
    return data

# Load data
data = load_data()

# Sidebar for product selection
products = data['Product'].unique()
selected_product = st.sidebar.selectbox('Selecione um produto:', products)

# Filter data for selected product
product_data = data[data['Product'] == selected_product]

# Create candlestick chart
fig = go.Figure(data=[
    go.Candlestick(
        x=product_data['Date'],
        open=product_data['UnitPrice'],
        high=product_data['TotalRevenue'],
        low=product_data['TotalCost'],
        close=product_data['Profit'],
        name='Candlestick'
    )
])

# Update layout
fig.update_layout(title=f'Análise de {selected_product}', xaxis_title='Data', yaxis_title='Valores')

# Show the figure
st.plotly_chart(fig)

# Display raw data
st.subheader('Dados Brutos')
st.write(product_data)