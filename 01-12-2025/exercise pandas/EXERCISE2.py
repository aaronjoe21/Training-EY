import pandas as pd
df=pd.read_csv("retail_sales.csv")

df["Date"]=pd.to_datetime(df["Date"])
df["Year"]=df["Date"].dt.year
df["Month"]=df["Date"].dt.month
df["Day"]=df["Date"].dt.year
print(df.head())