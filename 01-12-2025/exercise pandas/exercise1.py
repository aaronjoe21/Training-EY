import csv
import pandas as pd
df = pd.read_csv("retail_sales.csv")


#first 5 rows and last rows
print(df.head(5))
print(df.tail(5))

#column names
print(df.columns)

print(df.shape)