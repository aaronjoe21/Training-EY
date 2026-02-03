
import pandas as pd

df = pd.read_csv("retail.csv")
df.fillna({
    col: df[col].median() if df[col].dtype != 'object' else df[col].mode()[0]
    for col in df.columns
}, inplace=True)
