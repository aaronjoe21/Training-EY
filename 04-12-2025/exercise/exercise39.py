
import pandas as pd

files = ["file1.csv", "file2.csv", "file3.csv"]
df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True).drop_duplicates()

print(df)
