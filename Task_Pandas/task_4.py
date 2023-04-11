'''Для каждого спектрального класса вычислить дисперсию для Luminosity(L/Lo),
стандартная ошибка среднего для Absolute magnitude(Mv) и
среднеквадратичное отклонение для Temperature. На основе данных создать датафрейм и записать в excel файл.'''

import pandas as pd
import numpy as np
import xlwt



df = pd.read_csv("6 class csv.csv")

print(pd)
print(df.columns)
df = pd.read_csv("6 class csv.csv", usecols=['Temperature (K)', 'Luminosity(L/Lo)', 'Absolute magnitude(Mv)', 'Spectral Class'])
print(df.groupby('Spectral Class').var())

tar_tupe_var = df['Luminosity(L/Lo)'].var()
print(tar_tupe_var)
v_mean1 = df.groupby(['Temperature (K)', 'Luminosity(L/Lo)', 'Absolute magnitude(Mv)', 'Spectral Class']).std()
print(df.groupby(['Temperature (K)', 'Luminosity(L/Lo)', 'Absolute magnitude(Mv)', 'Spectral Class']).std())
v_mean_2 = str(df['Absolute magnitude(Mv)'].std())
print(df['Absolute magnitude(Mv)'].std())
v_mean_3 = df['Temperature (K)'].std()**2
print(v_mean_3)

df.to_excel(r'new_excel.xlsx')

