import pandas as pd
df = pd.read_csv("data.csv")

category_sales=df.groupby("SubCategory")["Quantity"].sum()
print(category_sales)