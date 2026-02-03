
import pandas as pd

df = pd.read_csv("retail.csv")

report = df.groupby("category").agg(
    total_sales=("price", "sum"),
    order_count=("order_id", "count"),
    avg_price=("price", "mean")
)
print(report)
