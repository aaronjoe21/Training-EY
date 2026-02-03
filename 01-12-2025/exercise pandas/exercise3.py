import pandas as pd
df = pd.read_csv("retail_sales.csv")


SUM=df.groupby("Store")["TotalPrice"].sum()
print(SUM)
SUM1=df.groupby("City")["TotalPrice"].sum()
print(SUM1)
SUM2=df.groupby("Category")["TotalPrice"].sum()
print(SUM2)