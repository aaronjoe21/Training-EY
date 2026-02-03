import pandas as pd
df = pd.read_csv("data.csv")


high_elec=df[(df["Returned"]=="Yes")]
print(high_elec["ProductName"])