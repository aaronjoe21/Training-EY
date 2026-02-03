import pandas as pd
df = pd.read_csv("data.csv")

category_sales=df.groupby("CustomerName")["OrderID"].count()
print(category_sales)