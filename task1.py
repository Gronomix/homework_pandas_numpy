'''Получить подробную информацию о датафрейме (count, mean, std, min, 25%, 50%, 75%, max). Полученный датафрейм
транспонировать. Также вывести список колонок датафрейма и информацию о типах данных колонок
датафрейма. На основе полученной информации создать датафрейм и записать его в формате JSON.'''

import pandas as pd
import numpy as np
import csv
from json import loads, dumps

df = pd.read_csv("Data_fr.csv")


print(df.info())

print(df.describe(), df.mean(), df.sum(), df.count(), df.std(), df.min())

print(f'{df.mean()} : среднее значение, /n, {df.sum()}: сумма значений, /n, '
      f"{df.count()} : колличество элементов, /n,"
      f'{df.std()} : среднеквадратичное отклонение'
      f'{df.count()} : количество элементов'
      f'{df.min()}, {df.max()} : минимальное значение и максимальное значение')

print(df.columns, df.dtypes)
reader = df.transpose()
print(reader)
result = reader.to_json()
pars = loads(result)
dumps(pars, indent=4)

print(pars)


