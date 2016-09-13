import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import seaborn as sns

# generate an array of x values
x = np.linspace(-15, 15, 400)

#compute the normalized intensity
norm_I = 4 * (scipy.special.j1(x) / x) ** 2

# plot computation
plt.close()
#gets rid of lines (default) and plots the actual points
plt.plot(x, norm_I, marker='.', linestyle='none')
#gives margins of 2%
plt.margins(0.02)
plt.xlabel('$x$')
plt.ylabel('$I(x) / I_0$')


#processing the spike data
# keyword arguments make sure that we skip the description and headings (skiprow)
# and split x and y values by specifying the delimiter
data = np.loadtxt('data/retina_spikes.csv', skiprows = 2, delimiter=',')
t = data[:,0]
V = data[:,1]

#close previous plots
plt.close()

#plot the data
plt.plot(t, V)
plt.xlabel('t (ms)')
plt.ylabel('V (uV)')

#change the range over which we look
plt.xlim(1395, 1400)
