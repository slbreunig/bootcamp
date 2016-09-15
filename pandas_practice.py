import numpy as np
import pandas as pd

#import data file
df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

# #get impact force for each frog
# frog_i_if = df[(df['ID'] == 'I')]['impact force (mN)']
# frog_ii_if = df[(df['ID'] == 'II')]['impact force (mN)']
# frog_iii_if = df[(df['ID'] == 'III')]['impact force (mN)']
# frog_iv_if = df[(df['ID'] == 'IV')]['impact force (mN)']
#
# #compute mean for all of the ipact factors for each frog
# mean_i = frog_i_if.mean()
# mean_ii = frog_ii_if.mean()
# mean_iii = frog_iii_if.mean()
# mean_iv = frog_iv_if.mean()
#
# print('Frog I: ', mean_i)
# print('Frog II: ', mean_ii)
# print('Frog III: ', mean_iii)
# print('Frog IV: ', mean_iv)

# #do this in a for loop:
# #initiate list
# num_list = ['I', 'II', 'III', 'IV']
# #make blank array
# impact_forces = np.empty(4)
#
# for i, number in enumerate(num_list):
#     frog_if = df[(df['ID'] == number)]['impact force (mN)']
#     impact_forces[i] = frog_if.mean()
#
# print (impact_forces)



#groupby() tutorial
#slice out ID's and impact forces
df_impf = df.loc[:, ['ID', 'impact force (mN)']]

#make GroupBy object
grouped = df_impf.groupby('ID')

#apply np.mean function to grouped object
df_mean_impf = grouped.apply(np.mean)

#look at new DataFrame
df_mean_impf
