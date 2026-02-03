import pandas as pd
df = pd.read_csv("data.csv")
df["OrderDate"]=pd.to_datetime(df["OrderDate"])
df["ShipDate"]=pd.to_datetime(df["ShipDate"])

df["ShippingDays"]=df["ShipDate"]-df["OrderDate"]
category_sales=df.groupby("Category")["ShippingDays"].mean()
print(category_sales)