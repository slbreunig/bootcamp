# Python Header
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import seaborn as sns
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18, 'axes.titlesize' : 18}
sns.set(rc=rc)

# This is not importing
import bootcamp_utils

# Load data
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

x_high, y_high = bootcamp_utils.ecdf(xa_high)
x_low, y_low = bootcamp_utils.ecdf(xa_low)

# Compute ideal gaussian distribution for each data set
x = np.linspace(1600, 2500, 400)
cdf_high = scipy.stats.norm.cdf(x, loc=np.mean(xa_high),
                                scale=np.std(xa_high))
cdf_low = scipy.stats.norm.cdf(x, loc=np.mean(xa_low),
                                scale=np.std(xa_low))

# Plot emperical data
plt.plot(x_high, y_high, marker='.', linestyle='none', markersize=20,
        alpha=0.5)
plt.plot(x_low, y_low, marker='.', linestyle='none', markersize=20,
        alpha=0.5)

# Plot computational data
plt.plot(x, cdf_high, color='gray')
plt.plot(x, cdf_low, color='gray')

# Add axes labels
plt.xlabel('Cross-sectional area (um)')
plt.ylabel('eCDF')

# Add a legend
plt.legend(('High Food', 'Low Food'), loc='lower right')

plt.show()
