'''Вычислить среднее значение колонки Temperature и добавить новую колонку delta_T,
в которой хранится модуль разности текущей Temperature и средней. Проверить содержит ли
датафрейм NaN значения. Вычислить максимальное значение Temperature. Вернуть датафрейм
в котором delta_T <= Tmax/2 и Temperature >= delta_Tmin. Полученный датафрейм сохранить в формате CSV.'''

import pandas as pd



df = pd.read_csv("6 class csv.csv", usecols=['Temperature (K)'])
print(df)
print(df.describe())

df["delta T"] = abs(df["Temperature (K)"] - df["Temperature (K)"].mean())
print(df)
t_max = df['Temperature (K)'].max()
print(t_max)
print(df.isnull())

df_new = df.drop(df[(df['Temperature (K)'] >= df["delta T"].min()) & (df['delta T'] <= df['Temperature (K)'].max() / 2)].index)

print(df_new.index)
print(df_new.describe())


df_new.to_csv('new.csv')





#df.to_csv(r"/path/to/filename.csv", index=False, sep=";")



#result_df = pd.merge(experiment_data, experiment_data_res,
                     #how="inner", on="Time")
#result_df
#print(df.describe())