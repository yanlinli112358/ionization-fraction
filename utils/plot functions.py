import matplotlib.pyplot as plt

from utils.math_functions import ionization_frac
def plot_log_ionization(c, pH, pKa):
    x = ionization_frac(c, pH, pKa)
    plt.xscale('log')
    plt.plot(c, x)
    plt.show()

