import pandas as pd
df = pd.read_csv("data.csv")
df["ShipDate"]=pd.to_datetime(df["ShipDate"])
high_elec=df[(df['Category'] == 'Furniture') & (df["ShipDate"]>'2024-1-20')]
print(high_elec)