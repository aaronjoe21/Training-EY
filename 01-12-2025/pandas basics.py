'''
import pandas as pd

s=pd.Series([10,20,30,40])
print(s)

data={
    "Name":["Aisha","Rahul","John"],
    "Marks":[85,92,78]
}

df=pd.DataFrame(data)
print(df)
'''
'''
import pandas as pd
data = {
    "Name":["Aisha","Rahul","John"],
    "Marks":[85,92,78],
    "City":["Mumbai","Delhi","Chennai"]
}
df=pd.DataFrame(data)
df.to_csv("student.csv",index=False)
print("CSV FILE CREATED")
'''
'''
import pandas as pd
df=pd.read_csv("student.csv")
print("CSV FILE READ SUCCESSFULLY")
print(df)
'''

import pandas as pd

df = pd.DataFrame({
    "Name": ["Aisha", "Rahul", "John", "Neha", "Imran"],
    "Marks": [85, 92, 78, 65, 55],
    "City": ["Mumbai", "Delhi", "Chennai", "Bangalore", "Hyderabad"],
    "Age": [22, 25, 23, 21, 24]
})
'''
print(df)

print(df.head(2)) ##top datas
print(df.tail(2)) ##bottom datas

print(df.shape) ##count of rows and columns
print(df.columns) ##names of columns
print(df.describe()) ##takes all numeric values and gives mena and evrything
'''
'''
##selecting
print(df["Name"])
print(df[["Name","Marks"]])

##filters
high_scorers=df[df["Marks"]>70]
print(high_scorers)

filtered=df[(df["Marks"]>70)&(df["Age"]>22)]
print(filtered)
'''
'''
##data
df["Result"]=df["Marks"].apply(lambda x :"Pass" if x>=60 else "FAIL)")
print(df)

sorted_df= df.sort_values(by="Marks", ascending=False)
print(sorted_df)
'''
'''
df2=df.copy()
df2.loc[2,"City"]=None ##to change value
print(df2)
print(df2.isnull().sum())   ##to count how many nulls in the table

df2_filled = df2.fillna("Unknown") ##to change the nulls to unknown
print(df2_filled)
'''

##group by
city_count=df.groupby("City")["Marks"].count()
print(city_count)
avg_marks=df.groupby("City")["Marks"].mean()
print(avg_marks)