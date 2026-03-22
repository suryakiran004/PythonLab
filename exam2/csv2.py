import pandas as pd

df = pd.read_csv("emp.csv")

print(df)


print(df.sort_values(by='name'))

print(df.sort_values(by='salary' , ascending=False))

print(df.groupby('institution')['salary'].max())