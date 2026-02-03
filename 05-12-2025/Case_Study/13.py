
import pymysql
import pandas as pd

conn = pymysql.connect(host="localhost", user="root", passwd="V@ishnav1", db="subscription_app", autocommit=True)
df = pd.read_sql("SELECT * FROM subscriptions", conn)

df["age_days"] = (pd.Timestamp.today() - pd.to_datetime(df["start_date"])).dt.days
print(df[["sub_id","customer_name","age_days"]].head())
