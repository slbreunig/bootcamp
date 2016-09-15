import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import bootcamp_utils as bcu
sns.set()

#specify parameters specific to our simulation
#number of generations; generation 1 = first cell
n_gen = 16

#chance of having a beneficial mutation
r = 1e-5

#total number of cells by the end
#number of cells in every generation is 2^(gen - 1)
n_cells = 2**(n_gen - 1)

#adaptive immunity: binomial distribution
ai_samples = np.random.binomial(n_cells, r, size=100000)

#report mean and std
print('AI mean: ', np.mean(ai_samples))
print('AI std: ', np.std(ai_samples))
print('AI Fano: ', np.var(ai_samples) / np.mean(ai_samples))

#function to draw out of random mutation hypothesis
def draw_random_mutation(n_gen, r):
    """Draw sample under random mutation hypothesis.
    Simulating what is happening for the random mutation
    hypothesis."""

    #initial number of mutants
    n_mut = 0

    #number of cells that can get mutations (daughter) = 2*(2^[g-1]-n-mut)
    #which equals 2^g - 2n_mut
    #did a binomial distribution - this is the type of distribution
    for g in range(n_gen):
        n_mut = 2*n_mut + np.random.binomial(2**g - 2*n_mut, r)

    return n_mut


def sample_random_mutation(n_gen, r, size=1):
    #initalize samples
    samples = np.empty(size)

    #draw the samples
    for i in range(size):
        samples[i] = draw_random_mutation(n_gen, r)

    return samples

#mean, std, fano for random mutation hypothesis
rm_samples = sample_random_mutation(n_gen, r, size=10000)
print ('RM mean: ', np.mean(rm_samples))
print('RM std: ', np.std(rm_samples))
print('RM Fano: ', np.var(rm_samples) / np.mean(rm_samples))

#define variables for the plot
x_ai, y_ai = bcu.ecdf(ai_samples)
x_rm, y_rm = bcu.ecdf(rm_samples)

#plot
plt.semilogx(x_rm, y_rm, marker='.', linestyle='none', alpha=0.5)
plt.semilogx(x_rm, y_rm, marker='.', linestyle='none', alpha=0.5)
plt.margins(0.02)
plt.xlabel('Number of Survivors')
plt.ylabel('CDF')

plt.show()
