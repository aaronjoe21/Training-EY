import pandas as pd
df=pd.read_csv("retail_sales.csv")



cash_orders = df[df["PaymentMethod"] == "Cash"].shape[0]
credit_orders = df[df["PaymentMethod"] == "Credit Card"].shape[0]
upi_orders = df[df["PaymentMethod"] == "UPI"].shape[0]

print(f"Cash: {cash_orders}, Credit Card: {credit_orders}, UPI: {upi_orders}")
