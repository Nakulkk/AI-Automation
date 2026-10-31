from pathlib import Path

import pandas as pd

data_file = Path(__file__).resolve().parent / 'StudentDetails.csv'
df = pd.read_csv(data_file)

print(df)

df.info()

print(df.shape)

print(df.head(2))

print(df.tail()) 

print(df.columns)

print(df.describe())  

print(df["name"])

print(df[["name", "ut1_marks"]])  