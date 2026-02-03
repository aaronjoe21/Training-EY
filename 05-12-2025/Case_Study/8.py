
import pymysql
import pandas as pd

conn = pymysql.connect(host="localhost", user="root", passwd="V@ishnav1", db="subscription_app", autocommit=True)
df = pd.read_sql("SELECT * FROM subscriptions", conn)
df["expiry_date"] = pd.to_datetime(df["expiry_date"])
df["days_left"]   = (df["expiry_date"] - pd.Timestamp.today()).dt.days
df["days_overdue"] = df["days_left"].apply(lambda d: abs(d) if d < 0 else 0)
print(df[["sub_id","customer_name","days_left","days_overdue"]].head())
