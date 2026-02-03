import pandas as pd
df = pd.read_csv("data.csv")

sorted_df = df.sort_values("CustomerName",ascending=True)
print(sorted_df["CustomerName"])
print(sorted_df)