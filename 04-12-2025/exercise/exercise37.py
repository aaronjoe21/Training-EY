
import pandas as pd

base = pd.read_csv("retail.csv")
base["month"] = pd.to_datetime(base["date"]).dt.month

df = base.pivot_table(
    values="price",
    index="category",
    columns="month",
    aggfunc="sum",
    fill_value=0
).reset_index()  # optional: make 'category' a normal column

print(df)
