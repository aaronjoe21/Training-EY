
import pymysql
import pandas as pd

conn = pymysql.connect(host="localhost", user="root", passwd="V@ishnav1", db="subscription_app", autocommit=True)
df = pd.read_sql("SELECT * FROM subscriptions", conn)

df["days_left"] = (pd.to_datetime(df["expiry_date"]) - pd.Timestamp.today()).dt.days

def status(d):
    if d < 0: return "Expired"
    if d <= 7: return "ExpiringSoon"
    return "Active"

df["status"] = df["days_left"].apply(status)
counts = df["status"].value_counts()
print(counts)
