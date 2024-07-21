import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

# Gerar dados de vendas
def generate_sales_data(num_records):
    sales_data = []
    for _ in range(num_records):
        sale = {
            'date': fake.date_this_year(),
            'item': fake.word(ext_word_list=['beer', 'wine', 'whiskey', 'cocktail', 'snack']),
            'quantity': np.random.randint(1, 5),
            'total_price': round(np.random.uniform(5, 30), 2)
        }
        sales_data.append(sale)
    return pd.DataFrame(sales_data)

# Gerar dados de clientes
def generate_customers_data(num_records):
    customers_data = []
    for _ in range(num_records):
        customer = {
            'name': fake.name(),
            'age': np.random.randint(18, 65),
            'gender': fake.random_element(elements=('M', 'F')),
            'visits_per_month': np.random.randint(1, 10)
        }
        customers_data.append(customer)
    return pd.DataFrame(customers_data)

# Gerar dados de localização do bar
def generate_location_data():
    return pd.DataFrame({
        'latitude': [fake.latitude()],
        'longitude': [fake.longitude()]
    })

sales_data = generate_sales_data(1000)
customers_data = generate_customers_data(100)
location_data = generate_location_data()

sales_data.to_csv('data/sales_data.csv', index=False)
customers_data.to_csv('data/customers_data.csv', index=False)
location_data.to_csv('data/location_data.csv', index=False)
