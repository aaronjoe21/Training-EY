import pandas as pd
customers = pd.read_csv("customers.csv")
orders = pd.read_csv("orders.csv")
merged = pd.merge(customers, orders, on="customer_id", how="inner")
print(merged.head())
