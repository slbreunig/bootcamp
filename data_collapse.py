import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import seaborn as sns
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18, 'axes.titlesize' : 18}
sns.set(rc=rc)

# Load files
wt_data = np.loadtxt('data/wt_lac.csv', delimiter=',',
                        skiprows=3)
q18m_data = np.loadtxt('data/q18m_lac.csv', delimiter=',',
                        skiprows=3)
q18a_data = np.loadtxt('data/q18a_lac.csv', delimiter=',',
                        skiprows=3)

# Slice out data from files into tuples
wt_iptg = wt_data[:,0]
wt_fc = wt_data[:,1]
q18m_iptg = q18m_data[:,0]
q18m_fc =  q18m_data[:,1]
q18a_iptg = q18a_data[:,0]
q18a_fc = q18a_data[:,1]

# # Plot data (IPTG vs Fold Change) - semilog x
# plt.semilogx(wt_iptg, wt_fc, linestyle='none', marker='.', markersize=10,
#         alpha=0.5)
# plt.semilogx(q18m_iptg, q18m_fc, linestyle='none', marker='.', markersize=10,
#         alpha=0.5)
# plt.semilogx(q18a_iptg, q18a_fc, linestyle='none', marker='.', markersize=10,
#         alpha=0.5)
# plt.xlabel('IPTG (mM)')
# plt.ylabel('Fold Change')
# plt.title('IPTG vs Fold Change')

# define R/K values (given)
wt_rk = 141.5
q18a_rk = 16.56
q18m_rk = 1332

# Compute theoretical fold change
def fold_change(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    num = RK * (1 + (c / KdA))**2
    denom_1 = (1 + (c/KdA))**2
    denom_2 = Kswitch * (1 + (c / KdI))**2
    calc_fold_change = (1 + num/(denom_1 + denom_2))**(-1)
    return calc_fold_change

# Generate a list of IPTG concentrations for calc's
x = np.logspace(-6, 2, 500)

# Calculate theoretical fold change
wt_calc = fold_change(x, wt_rk)
q18a_calc = fold_change(x, q18a_rk)
q18m_calc = fold_change(x, q18m_rk)

# # Plot theoretical curves
# plt.plot(x, wt_calc, 'b-', linewidth=0.5)
# plt.plot(x, q18a_calc, 'r-', linewidth=0.5)
# plt.plot(x, q18m_calc, 'g-', linewidth=0.5)
#
# # Add a legend
# plt.legend(('wt', 'q18a', 'q18m'), loc = 'upper left')

#plt.show()

# Compute Bohr parameter
def bohr_parameter(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    first_term = (-1) * np.log(RK)
    num = (1 + (c/KdA))**2
    denom_1 = (1 + (c/KdA))**2
    denom_2 = Kswitch * (1 + (c / KdI))**2
    second_term = (-1) * np.log(num / (denom_1 + denom_2))
    return first_term + second_term

# Compute Calc'd fold change based on Bohr parameter
def fold_change_bohr(bohr_parameter):
    denom = 1 + np.exp((-1) * bohr_parameter)
    return (1 / denom)

# Generate Bohr values range(-6, 6)
bohr_input = np.linspace(-6, 6, 500)
# Generate Bohr values using IPTG conc's
bohr_par_wt = bohr_parameter(wt_iptg, wt_rk)
bohr_par_q18m = bohr_parameter(q18m_iptg, q18m_rk)
bohr_par_q18a = bohr_parameter(q18a_iptg, q18a_rk)

# Compute Bohr theoretical fold change
bohr_fold_change = fold_change_bohr(bohr_input)

# Plot theoretical Bohr values
plt.plot(bohr_input, bohr_fold_change, color='gray')
# Plot experimental Bohr values
plt.plot(bohr_par_wt, fold_change_bohr(bohr_par_wt), 'b', linestyle='none',
        marker='.', markersize=10)
plt.plot(bohr_par_q18a, fold_change_bohr(bohr_par_q18a), 'r', linestyle='none',
        marker='.', markersize=10)
plt.plot(bohr_par_q18m, fold_change_bohr(bohr_par_q18m), 'g', linestyle='none',
        marker='.', markersize=10)

#Bohr plot formatting
plt.xlabel('Bohr Parameter')
plt.ylabel('Fold Change')
plt.title('Data Collapse')
plt.legend(('Theoretical', 'wt', 'q18a', 'q18m'), loc="upper left")

plt.show()
