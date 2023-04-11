'''Вычислить коэффициент корреляции датафрейма.
Вычислить среднее значение Absolute magnitude(Mv) для каждого Star type.
Вычислить количество записей для каждого спектрального класса'''


import pandas as pd
import numpy as np
from pandas import DataFrame


df = pd.read_csv("6 class csv.csv")

print(pd)
print(df.columns)
df = pd.read_csv("6 class csv.csv", usecols=['Absolute magnitude(Mv)', 'Star type', 'Spectral Class'])
print(df)
x = df[['Absolute magnitude(Mv)', 'Star type']]
x.corr()
print(x.corr())
print(df['Star type'].corr(df['Absolute magnitude(Mv)']))

print(df.describe())

unik_val_spektrClass = df['Spectral Class'].value_counts()
print(unik_val_spektrClass)

star_tupe_mean = df.groupby('Absolute magnitude(Mv)').mean('Star type')
print(star_tupe_mean)


