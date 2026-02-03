
import pandas as pd

df = pd.read_csv("retail.csv")
df["DiscountedPrice"] = df["price"] * 0.9

print(df.head())                          # quick check
df.to_csv("retail_with_discount.csv", index=False)
