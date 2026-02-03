import pandas as pd
df = pd.read_csv("data.csv")

category_sales=df.groupby("Region")["Sales"].sum()
print(category_sales)