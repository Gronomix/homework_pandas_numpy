'''Для каждого спектрального класса вычислить дисперсию для Luminosity(L/Lo),
стандартная ошибка среднего для Absolute magnitude(Mv) и
среднеквадратичное отклонение для Temperature. На основе данных создать датафрейм и записать в excel файл.'''

import pandas as pd
import numpy as np
from pandas import DataFrame


df = pd.read_csv("6 class csv.csv")

print(pd)
print(df.columns)
df = pd.read_csv("6 class csv.csv", usecols=['Temperature (K)', 'Luminosity(L/Lo)', 'Absolute magnitude(Mv)', 'Spectral Class'])
print(df.groupby('Spectral Class').var())

tar_tupe_var = df['Luminosity(L/Lo)'].var()
print(tar_tupe_var)

