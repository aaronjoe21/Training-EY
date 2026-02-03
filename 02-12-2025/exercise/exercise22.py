import pandas as pd
df = pd.read_csv("data.csv")

category_sales=df.groupby("Category")["Profit"].mean()
print(category_sales)