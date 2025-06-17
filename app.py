import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

# Plotting
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot Units Sold
ax1.set_xlabel('Data')
ax1.set_ylabel('Unidades Vendidas', color='tab:blue')
ax1.plot(product_data['Date'], product_data['UnitsSold'], color='tab:blue', label='Unidades Vendidas')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Create a second y-axis for Revenue
ax2 = ax1.twinx()  
ax2.set_ylabel('Receita', color='tab:orange')  
ax2.plot(product_data['Date'], product_data['TotalRevenue'], color='tab:orange', label='Receita')
ax2.tick_params(axis='y', labelcolor='tab:orange')

# Create a third y-axis for Profit
ax3 = ax1.twinx()  
ax3.spines['right'].set_position(('outward', 60))  
ax3.set_ylabel('Lucro', color='tab:green')  
ax3.plot(product_data['Date'], product_data['Profit'], color='tab:green', label='Lucro')
ax3.tick_params(axis='y', labelcolor='tab:green')

# Title and layout
plt.title(f'Análise de {selected_product}')
fig.tight_layout()  
st.pyplot(fig)

# Display raw data
st.subheader('Dados Brutos')
st.write(product_data)