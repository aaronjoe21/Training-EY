import pandas as pd

df = pd.read_csv("retail_sales.csv")
df["Discount"]=df.apply(lambda x : x["TotalPrice"]* (0.90 if x["CustomerType"]=='Returning' else 0.95),axis=1)
print(df)