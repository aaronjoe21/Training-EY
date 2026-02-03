import pandas as pd
df = pd.read_csv("data.csv")

high_elec=df[(df["Category"]=="Technology")&(df["Sales"]>400)]
print(high_elec)