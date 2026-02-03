import pandas as pd
df = pd.read_csv("data.csv")

high_elec=df[(df['Profit'] < 20)]
print(high_elec)