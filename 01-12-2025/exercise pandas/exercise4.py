import pandas as pd
df = pd.read_csv("retail_sales.csv")
sort=df.sort_values(by="TotalPrice", ascending=False)
print(sort.head(5))