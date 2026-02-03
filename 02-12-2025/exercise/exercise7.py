
import pandas as pd
df = pd.read_csv("data.csv")

df["ProfitMargin"]=df["Profit"]/df["Sales"]
print(df)