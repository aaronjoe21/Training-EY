'''
import pandas as pd

df = pd.DataFrame({
    "Name":["Aisha","Rahul","John"],
    "Marks":[85,92,78],
    "City":["Mumbai","Delhi","Chennai"]
#write to JSON file
df.to_json("student.json",orient="records",indent=4)

print("JSON file created")

#read the same json file
df=pd.read_json("student.json")

print("JSON file read successfully")
print(df)
})
'''
'''
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Aisha", "Rahul", "John", "Neha", "Imran"],
    "Marks": [85, None, 78, None, 55],
    "City": ["Mumbai", "Delhi", None, "Bangalore", None],
    "Age": [22, 25, None, 21, 24]
})

print(df)
#returns true to the Nulls on each column
print(df.isnull())
#gives the count of nulls
print(df.isnull().sum())
#replaces
print(df.replace("",None).isnull().sum())
'''

import pandas as pd

df=pd.read_csv("retail_50.csv")
'''
print(df.head()
      
#date is object but it is supposed to be datatime format
print(df.info()) #gives info
print(df.describe()) # describes numerical coulmns
df["Date"]=pd.to_datetime(df["Date"]) #converst date into datetime format instead of object
print(df.info())

#making date into 3 columns of year,month,day
df["Year"]=df["Date"].dt.year
df["Month"]=df["Date"].dt.month
df["Day]"]=df["Date"].dt.day
print(df)
'''
'''
##this filters electronics and price above 10000
high_elec=df[(df["Category"]=="Electronics")&(df["TotalPrice"]>10000)]
print(high_elec)

#sorting
sorted_df = df.sort_values("TotalPrice",ascending=False)

#to gorup each category with corresponding total price
category_sales=df.groupby("Category")["TotalPrice"].sum()
print(category_sales)

#to group stores along with its average prices
store_avg=df.groupby("Store")["TotalPrice"].mean()
print(store_avg)
#to group citys with no of orders along with it
city_orders=df.groupby("City")["OrderID"].count()
print(city_orders)
'''

customers=pd.DataFrame({
    "CustomerType":["New","Returning"],
    "Discount":[5,10]
})

merged=df.merge(customers,on="CustomerType",how="left")
print(merged)



