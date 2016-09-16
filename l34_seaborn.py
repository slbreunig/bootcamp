import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#import data
df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')
#rename column
df = df.rename(columns={'impact force (mN)': 'impf'})
 #mean impact force of frog I
 #bool for frog one, slice out impact force
 np.mean(df.loc[df['ID'] == 'I', 'impf'])

#computes all means and standard errors of the mean
mean_impf = np.empty(4)
sem_impf = np.empty(4)
for i, frog in enumerate(['I', 'II', 'III', 'IV']):
    mean_impf[i] = np.mean(df.loc[df['ID']==frog, 'impf'])
    n = np.sum(df['ID']=='I')
    sem_impf[i] = np.std(df.loc[df['ID']==frog, 'impf']) / np.sqrt(n)

print(mean_impf)
print(sem_impf)

#making the bar graph with error bars:
plt.bar(np.arange(4), mean_impf, yerr=sem_impf, ecolor='black',
        tick_label=['I', 'II', 'III', 'IV'], align='center')
plt.ylabel('impact force (mN)')

#much easier with GroupBy!!!!
#create groupby object
#splits up frogs by the ID - eg by frog I, frog II, etc
gb_frog = df.groupby('ID')

mean_impf = gp_frog['impf'].mean()
#now typing in mean_impf returns a list of all of the mean impf's,
#organized for each frog
#can also do with standard error of the mean [.sem()]

#now to make same bar graph using seaborn (need a tidy dataframe):
sns.barplot(data=df, x='ID', y='impf')
#also chooses labels for you - here we are overriding these choices
plt.xlabel('')
plt.ylabel('impact force (mN)')


#making a swarm plot using seaborn:
sns.swarmplot(data=df, x='ID', y='impf')

#colors points based on date
sns.swarmplot(data=df, x='ID', y='impf', hue='date')
#removes ugly legend
pla.gca().legend_.remove()

#too much data for a swarm plot: use boxplot
sns.boxplot(data=df, x='ID', y='impf')
#line in middle is median
#edges are 25th and 75th percentile
#(these are all independent of distribution)
#whiskers tell largest data point (extent of data)
#or up to length of interquartile range (iqr)
#individual points (outliers) are shown if outside of iqr 
