""" Solves the predator-prey differential equation using the
Lotka-Volterra model. Foxes (f) are the predators, and Rabbits (r)
are the prey. """

# General initiation
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import seaborn as sns
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18, 'axes.titlesize' : 18}
sns.set(rc=rc)

# Specifiy parameters
alpha = 1
beta = 0.2
delta = 0.3
gamma = 0.8
delta_t = 0.001
t = np.arange(0, 60, delta_t)

# Arrays for number of rabbits and foxes
r = np.empty_like(t)
f = np.empty_like(t)

# Initial values
r[0] = 10
f[0] = 1

# For loop to update populations
for i in range(1, len(t)):
