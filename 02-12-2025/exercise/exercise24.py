import pandas as pd
df = pd.read_csv("data.csv")

category_sales=df.groupby("Segment")["Sales"].sum()
print(category_sales)