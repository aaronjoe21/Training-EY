
import pymysql
import pandas as pd

conn = pymysql.connect(host="localhost", user="root", passwd="V@ishnav1", db="subscription_app", autocommit=True)
df = pd.read_sql("SELECT * FROM subscriptions", conn)

df["next_billing_date"] = pd.to_datetime(df["expiry_date"]).dt.date  # simple: same as expiry
print(df[["sub_id","customer_name","next_billing_date"]].head())
