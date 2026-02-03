import pandas as pd

df = pd.read_csv('retail_sales.csv')

sorted_df = df.sort_values("Date", ascending=True)

final_sort = sorted_df.sort_values("TotalPrice", ascending=False)
print(final_sort[["Date", "TotalPrice"]])