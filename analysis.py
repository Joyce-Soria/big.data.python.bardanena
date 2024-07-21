import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import plotly.express as px

# Carregar dados
sales_data = pd.read_csv('../data/sales_data.csv')
customers_data = pd.read_csv('../data/customers_data.csv')
location_data = pd.read_csv('../data/location_data.csv')

# Processamento de dados
sales_data['date'] = pd.to_datetime(sales_data['date'])
sales_data['month'] = sales_data['date'].dt.to_period('M')

# Análise de vendas por mês
sales_per_month = sales_data.groupby('month').agg({'total_price': 'sum'}).reset_index()

# Previsão de clientes para o próximo mês
model = LinearRegression()
X = np.array(range(len(sales_per_month))).reshape(-1, 1)
y = sales_per_month['total_price'].values
model.fit(X, y)
next_month_prediction = model.predict([[len(sales_per_month)]])

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

fig_sales_per_month.show()
fig_customers_age_distribution.show()
fig_location.show()
