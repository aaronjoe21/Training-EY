import pandas as pd

df = pd.read_csv("retail_sales.csv")

grouped_df = df.groupby("OrderID")["TotalPrice"].mean()
print(grouped_df)