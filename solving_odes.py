""" Problem 3.3 16.9.13 tutorial """

# General initiation
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import seaborn as sns
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18, 'axes.titlesize' : 18}
sns.set(rc=rc)

# Specify parameter
k = 1

# Specify my time step
delta_t = 0.01

# Make an array of time points, evenly spaced to 10
t = np.arange(0, 10, delta_t)

# Make an array to store the number of bacteria
n = np.empty_like(t)

# Set initial number of bacteria
n[0] = 1

# Write a for loop to keep updating n as time goes on
for i in range(1, len(t)):
    n[i] = n[i-1] + delta_t * k * n[i-1]

# Make a plot for this simulated data
plt.plot(t, n)
plt.margins(0.02)
plt.xlabel('time')
plt.ylabel('number of bacteria')

plt.show()
