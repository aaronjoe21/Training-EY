
import pymysql
import pandas as pd

conn = pymysql.connect(host="localhost", user="root", passwd="V@ishnav1", db="subscription_app", autocommit=True)
df = pd.read_sql("SELECT * FROM subscriptions", conn)

# Ensure computed fields exist (status, days_left, age_days, renewal_value, next_billing_date)
df["start_date"]  = pd.to_datetime(df["start_date"])
df["expiry_date"] = pd.to_datetime(df["expiry_date"])
df["days_left"]   = (df["expiry_date"] - pd.Timestamp.today()).dt.days
df["age_days"]    = (pd.Timestamp.today() - df["start_date"]).dt.days
df["next_billing_date"] = df["expiry_date"].dt.date

def status(d):
    if d < 0: return "Expired"
    if d <= 7: return "ExpiringSoon"
    return "Active"
df["status"] = df["days_left"].apply(status)

price_map = {"Monthly": 1000, "Quarterly": 2700, "Yearly": 10000}
df["renewal_value"] = df["plan_type"].map(price_map).fillna(0)

df.to_csv("subscription_report.csv", index=False)
print("Saved: subscription_report.csv")
