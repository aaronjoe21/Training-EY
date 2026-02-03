import pandas as pd
df = pd.read_csv("data.csv")
df["ProfitMargin"]=df["Profit"]/df["Sales"]
sorted_df = df.sort_values("ProfitMargin",ascending=False)
print(sorted_df)