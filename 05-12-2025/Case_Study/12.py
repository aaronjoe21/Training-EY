
import pymysql
import pandas as pd

conn = pymysql.connect(host="localhost", user="root", passwd="V@ishnav1", db="subscription_app", autocommit=True)
df = pd.read_sql("SELECT * FROM subscriptions", conn)


df["expiry_date"] = pd.to_datetime(df["expiry_date"])
df["days_left"] = (df["expiry_date"] - pd.Timestamp.today()).dt.days

# 2) Build the reminder list (<= 5 days)
reminders = df[df["days_left"] <= 5][
    ["sub_id", "customer_name", "plan_type", "expiry_date", "days_left"]
].sort_values("days_left")

print(reminders)
