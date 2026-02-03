
import pymysql
import pandas as pd

conn = pymysql.connect(host="localhost", user="root", passwd="V@ishnav1", db="subscription_app", autocommit=True)
df = pd.read_sql("SELECT * FROM subscriptions", conn)

df["next_billing_date"] = pd.to_datetime(df["expiry_date"]).dt.date


today_date = pd.Timestamp.today().date()
due_today = df[pd.to_datetime(df["next_billing_date"]).dt.date == today_date][
    ["sub_id","customer_name","plan_type","next_billing_date"]
]
print(due_today)
