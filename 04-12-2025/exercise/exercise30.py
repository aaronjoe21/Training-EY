import pandas as pd

df = pd.read_csv("retail.csv")
print("Total Orders:", df["order_id"].nunique())
print("Total Revenue:", (df["price"] * df["quantity"]).sum())
print("Top 5 Products:\n", df["product"].value_counts().head(5))
