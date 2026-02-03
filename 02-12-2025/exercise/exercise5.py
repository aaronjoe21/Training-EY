
import pandas as pd
df = pd.read_csv("data.csv")

df["OrderDate"]=pd.to_datetime(df["OrderDate"]) #converst date into datetime format instead of object
print(df.info())