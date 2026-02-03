import pandas as pd
df = pd.read_csv("data.csv")

df = df[df['Sales'] > 0]
print(df)
