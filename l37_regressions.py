import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import scipy.optimize

df = pd.read_csv('data/bcd_gradient.csv', comment='#')
df = df.rename(columns={'fractional distance from anterior': 'x',
                '[bcd] (a.u.)': 'I_bcd'})
plt.plot(df['x'], df['I_bcd'], marker='.', linestyle='none')

#definie a function for modeling the gradient
#use predefined function that the data should fit/we are testing
def gradient_model(x, I_0, a, lam):
    """model for bcd gradient: exponential decay plus background"""
    #make sure program works
    if np.any(np.array(x) <= 0):
        raise RuntimeError('x must be positive')
    if np.any(np.array([I_0, a, lam]) < 0):
        raise RuntimeError('all parameters must be positive')
    return a + I_0 * np.exp(-x / lam)

#runtime errors might arise if program starts to look at negative values
#even if given parameters are positive. It can wander off into regions
#that are not physically possible
#easly fix: use logs/exponentiation of the function - now won't get neg values

a_guess = 0.2
I_0_guess = 0.9 - 0.2
lam_guess = 0.25
#construct an array of our guesses for the parameters
p0 = np.array([I_0_guess, a_guess, lam_guess])

#will output parameters as an array
popt, _ = scipy.optimize.curve_fit(gradient_model, df['x'], df['I_bcd'], p0=p0)

#split up parameters from an array into a tuple
#plot the parameters into a smooth line
x_smooth = np.linspace (0, 1, 200)
I_smooth = gradient_model(x_smooth, *tuple(popt))
plt.plot(x_smooth, I_smooth, color='gray')
