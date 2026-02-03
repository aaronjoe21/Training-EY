import pandas as pd
df = pd.read_csv("retail_sales.csv")
Total_quantity = df.groupby("Category")["Quantity"].sum()  # To calculate no. of orders grouped by orderID
print(Total_quantity)
Total_Revenue = df.groupby("Category")["TotalPrice"].sum()
print(Total_Revenue)
