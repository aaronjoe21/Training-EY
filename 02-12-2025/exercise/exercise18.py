import pandas as pd
df = pd.read_csv("data.csv")

sorted_df = df.sort_values("Region",ascending=False)
print(sorted_df)

sorted_df = df.sort_values("City",ascending=False)
print(sorted_df)