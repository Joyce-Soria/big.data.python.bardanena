import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados
sales_data = pd.read_csv('../data/sales_data.csv')
customers_data = pd.read_csv('../data/customers_data.csv')
location_data = pd.read_csv('../data/location_data.csv')

# Processamento de dados
sales_data['date'] = pd.to_datetime(sales_data['date'])
sales_data['month'] = sales_data['date'].dt.to_period('M')
sales_per_month = sales_data.groupby('month').agg({'total_price': 'sum'}).reset_index()

# Visualização de vendas por mês
fig_sales_per_month = px.line(sales_per_month, x='month', y='total_price', title='Vendas por Mês')

# Análise de dados de clientes
fig_customers_age_distribution = px.histogram(customers_data, x='age', title='Distribuição de Idade dos Clientes')

# Mapa de localização do bar
fig_location = px.scatter_mapbox(
    location_data,
    lat='latitude',
    lon='longitude',
    zoom=15,
    title='Localização do Bar da Nena'
)
fig_location.update_layout(mapbox_style="open-street-map")

# Streamlit interface
st.title('Análise de Dados do Bar da Nena')
st.write('Este projeto é um estudo de caso de Big Data e Power BI aplicado ao Bar da Nena.')

st.header('Vendas por Mês')
st.plotly_chart(fig_sales_per_month)

st.header('Distribuição de Idade dos Clientes')
st.plotly_chart(fig_customers_age_distribution)

st.header('Localização do Bar')
st.plotly_chart(fig_location)

if st.button('Previsão de Clientes para o Próximo Mês'):
    st.write(f'Previsão de clientes para o próximo mês: {next_month_prediction[0]:.2f}')
