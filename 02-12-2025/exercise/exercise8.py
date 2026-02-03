

import pandas as pd
df = pd.read_csv("data.csv")

df["CustomerName"]=df["CustomerName"].str.title()
print(df["CustomerName"])