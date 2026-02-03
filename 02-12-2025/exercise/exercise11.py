import pandas as pd
df = pd.read_csv("data.csv")

high_elec=df[(df["Region"]=="West")]
print(high_elec)
