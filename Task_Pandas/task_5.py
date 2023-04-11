'''На основании датасета df создать новый датафрейм new_df с двумя колонками Temperature и temperature_C, где

new_df["Temperature"] = df["Temperature"]

а в колонке temperature_C хранится значение температуры в С.

Соединить два датафрейма в один, как минимум тремя разными способами.

После соединения проверить датафрейм на наличие NaN значений. Заменить отсутствующие данные следующими способами:

Для всех NaN значений установить среднее значение столбца.

Заменить NaN значения с помощью интерполяции.

Удалить строки содержащие NaN значения.'''

import pandas as pd

df = pd.read_csv("6 class csv.csv")


print(df.columns)
df = pd.read_csv("6 class csv.csv", usecols=['Temperature (K)'])
print(df)
new_df = df[["Temperature (K)"]]. copy()
new_df['Temperature C'] = abs(df["Temperature (K)"] - 273.15)
print(new_df)
new_df.to_excel('temperature.xlsx')

result_df_left = pd.merge(df, new_df, how="left", on='Temperature (K)')
print(result_df_left)
result_df_other = pd.merge(new_df, df, how="outer", on="Temperature (K)")
print(result_df_other)
column_result_df = pd.concat([df, new_df], axis=0)
print(column_result_df)
column_result_df["Temperature (K)"] = column_result_df["Temperature (K)"].fillna(column_result_df["Temperature (K)"].mean())

column_result_df["Temperature C"] = column_result_df["Temperature C"].fillna(column_result_df["Temperature C"].mean())
print(column_result_df)
result_df_other.interpolate(method='pad', limit=2)
print(result_df_other)

t = result_df_left.dropna(axis=0)
print(t)