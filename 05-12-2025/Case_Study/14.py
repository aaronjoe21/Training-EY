
import pymysql
import pandas as pd

conn = pymysql.connect(host="localhost", user="root", passwd="V@ishnav1", db="subscription_app", autocommit=True)
df = pd.read_sql("SELECT * FROM subscriptions", conn)

price_map = {"Monthly": 1000, "Quarterly": 2700, "Yearly": 10000}
df["renewal_value"] = df["plan_type"].map(price_map).fillna(0)
df["age_days"] = (pd.Timestamp.today() - pd.to_datetime(df["start_date"])).dt.days

plan_rollup = df.groupby("plan_type").agg(
    total_customers=("sub_id","count"),
    average_age_days=("age_days","mean"),
    expected_renewal_revenue=("renewal_value","sum")
).reset_index()

print(plan_rollup)
