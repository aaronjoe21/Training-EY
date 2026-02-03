import pandas as pd

df = pd.read_csv('retail_sales.csv')

filtered_df = df[df['Product'].str.contains('a', case=False, na=False)]
print(filtered_df["Product"])