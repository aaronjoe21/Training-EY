import pandas as pd
df = pd.read_csv("data.csv")
df = pd.read_csv("data.csv")
df["OrderDate"]=pd.to_datetime(df["OrderDate"])
df["ShipDate"]=pd.to_datetime(df["ShipDate"])

df["ShippingDays"]=df["ShipDate"]-df["OrderDate"]
sorted_df = df.sort_values("ShippingDays",ascending=False)
print(sorted_df)