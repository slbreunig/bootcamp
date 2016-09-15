import numpy as np
import bootcamp_utils as bcu
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#load data
bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

#generate x and y values for ecdf plot
x_1975, y_1975 = bcu.ecdf(bd_1975)
x_2012, y_2012 = bcu.ecdf(bd_2012)

#generate ecdf plots
plt.plot(x_1975, y_1975, color='blue', linestyle='none'))

for i in range(100):
    #generate a bootstrap sample
    bs_sample = np.random.choice(bd_1975, replace=True, size=10000)
    x_bs, y_bs = bcu.ecdf(bs_sample)
    plt.plot(x_bs, y_bs, color='blue', alpha=0.01, linestyle='none')

plt.show()
