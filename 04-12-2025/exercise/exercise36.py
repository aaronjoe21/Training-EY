
import pandas as pd

base = pd.read_csv("retail.csv")
base["total"] = base["price"] * base["quantity"]

df = (base.groupby("customer_id", as_index=False)["total"]
         .sum()
         .query("total > 5000")
         .rename(columns={"total": "total_spent"}))

print(df)
