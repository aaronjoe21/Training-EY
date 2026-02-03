
import pandas as pd

base = pd.read_csv("retail.csv")

Q1 = base["price"].quantile(0.25)
Q3 = base["price"].quantile(0.75)
IQR = Q3 - Q1

df = base[(base["price"] >= Q1 - 1.5 * IQR) & (base["price"] <= Q3 + 1.5 * IQR)].copy()

print(df)
