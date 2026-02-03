import pandas as pd
df = pd.read_csv("data.csv")

df['Discount'] = (df['Discount'] * 100)
print(df['Discount'])

