
import pymysql
import pandas as pd

conn = pymysql.connect(host="localhost", user="root", passwd="V@ishnav1", db="subscription_app", autocommit=True)
df = pd.read_sql("SELECT * FROM subscriptions", conn)
df["created_at"] = pd.to_datetime(df["created_at"])
df["created_at_fmt"] = df["created_at"].dt.strftime("%d-%m-%Y %H:%M")
print(df[["sub_id","customer_name","created_at_fmt"]].head())
