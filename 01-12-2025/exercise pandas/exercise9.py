import pandas as pd

df = pd.read_csv('retail_sales.csv')

sorted_df = df.sort_values("TotalPrice", ascending=False)
grouped_df = sorted_df.groupby("Store")["TotalPrice"].sum()
print(grouped_df.head(1))