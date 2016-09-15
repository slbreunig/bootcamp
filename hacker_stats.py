import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

# bs = BootStrap
# don't have to just do mean; can do any statstical calculation
# GENERATING CONFIDENCE INTERVALS
# can change .mean to .std (etc) to determine the standard deviation
# confidence intervals rather than those for the mean

# Generate a bunch of bootsrap replicates
# each bs_sample pulls number in set amount from a distribution of the
#initial data set, with replacement. The mean of each of these sample sets
#is computed, and then the process is repeated n_reps times.
#A distribution can then be generated.
n_reps = 100000
bs_replicates_1975 = np.empty(n_reps)
for i in range(n_reps):
    bs_sample = np.random.choice(bd_1975, replace=True, size=len(bd_1975))
    bs_replicates_1975[i] = np.mean(bs_sample)

# Confidence interval for the 1975 data
#2.5 and 97.5 correspond to making a 95% confidence interval
conf_int_1975 = np.percentile(bs_replicates_1975, [2.5, 97.5])


# Repeat for the 2012 data
n_reps = 100000
bs_replicates_2012 = np.empty(n_reps)
for i in range(n_reps):
    bs_sample = np.random.choice(bd_2012, replace=True, size=len(bd_2012))
    bs_replicates_2012[i] = np.mean(bs_sample)

conf_int_2012 = np.percentile(bs_replicates_2012, [2.5, 97.5])

def ecdf(data):
    return np.sort(data), np.arange(1, len(data)+1) / len(data)

# x_1975, y_1975 = ecdf(bd_1975)
# x_2012, y_2012 = ecdf(bd_2012)
# x_1975_bs, y_1975_bs = ecdf(bs_sample)
#
# plt.plot(x_1975, y_1975, marker='.', linestyle='none', alpha=0.5)
# plt.plot(x_1975_bs, y_1975_bs, marker='.', linestyle='none', alpha=0.5)
# plt.xlabel('Beak Depth (mm)')
# plt.ylabel('EDCF')
# plt.legend(('1975', '1975 bootstrap'), loc='lower right')
# plt.show()
