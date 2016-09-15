import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import bootcamp_utils as bcu
sns.set()

#load data frames
df_1973 = pd.read_csv('data/grant_1973.csv', comment='#')
df_1975 = pd.read_csv('data/grant_1975.csv', comment='#')
df_1987 = pd.read_csv('data/grant_1987.csv', comment='#')
df_1991 = pd.read_csv('data/grant_1991.csv', comment='#')

#reformat data
#rename column headings
df_1973 = df_1973.rename(columns = {'yearband':'year', 'beak length':
            'beak length (mm)', 'beak depth' : 'beak depth (mm)'})
df_1975 = df_1975.rename(columns = {'Beak length, mm': 'beak length (mm)',
            'Beak depth, mm' : 'beak depth (mm)'})
df_1987 = df_1987.rename(columns = {'Beak length, mm': 'beak length (mm)',
            'Beak depth, mm' : 'beak depth (mm)'})
df_1991 = df_1991.rename(columns = {'blength': 'beak length (mm)',
            'bdepth' : 'beak depth (mm)'})

#reformat years
df_1973 = df_1973.replace('73', '1973')

#add data columns for years to 1975, 1987, 1991
#create columns - function
def create_year_col(data_frame, year):
    year_list = {}
    for i in range(len(data_frame)):
        year_list[i] = year
    return pd.Series(year_list)

#execute function to create columns
df_1975_year = create_year_col(df_1975, '1975')
df_1987_year = create_year_col(df_1987, '1987')
df_1991_year = create_year_col(df_1991, '1991')
#add columns for each year (concatenate dataframes)
df_1975 = pd.concat((df_1975, df_1975_year), axis=1)
df_1987 = pd.concat((df_1987, df_1987_year), axis=1)
df_1991 = pd.concat((df_1991, df_1991_year), axis=1)
#rename/create headers for each year column
df_1975 = df_1975.rename(columns={0: 'year'})
df_1987 = df_1987.rename(columns={0: 'year'})
df_1991 = df_1991.rename(columns={0: 'year'})

#remove duplicates
df_1973.drop_duplicates(['band'])
df_1975.drop_duplicates(['band'])
df_1987.drop_duplicates(['band'])
df_1991.drop_duplicates(['band'])

#merge into one data frame
df_1 = pd.concat((df_1973, df_1975))
df_2 = pd.concat((df_1987, df_1991))
df = pd.concat((df_1, df_2), ignore_index=True)
df = df[['year', 'band', 'species', 'beak depth (mm)', 'beak length (mm)']]
