import pandas as pd
import csv

df = pd.read_csv("kainos.csv", usecols = ['Kaina'])

print(df)

rounded_price = []

for i in df:

    round_price = round(((round((int(df[i]) * 1.21), 0)) / 1.21), 2)
    rounded_price.append(round_price)

df_2 = pd.read_csv("kainos.csv")

for i in rounded_price:

    df_2.loc[i, 'Kaina'] = rounded_price[i]
    df_2.to_csv("kainos.csv", index = False)

