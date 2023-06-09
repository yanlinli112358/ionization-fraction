import numpy as np
import matplotlib.pyplot as plt

from utils.math_functions import ionization_frac
salt_conc = np.linspace(0, 2e-3, 100)
pH = 5.7
pKa = 10.5
x = ionization_frac(salt_conc, pH, pKa)

conc_Br = 1e-3 * np.array([0.05, 0.1, 0.15, 0.2, 0.25,
                           0.3, 0.4, 0.5, 0.6, 0.75])
ion_cov = [0.1056, 0.12958, 0.31523, 0.3315, 0.33966,
           0.36186, 0.3975, 0.41055, 0.5936, 0.63248]

conc_Br_isotherm = 1e-3 * np.array([0, 0.05, 0.1, 0.15, 0.2, 0.25,
                    0.3, 0.4, 0.5, 0.6, 0.75, 1, 1.5, 2])
kink_pressure = [2.371, 7.263, 10.348, 13.2, 15.022, 17.646,
                 18.065, 22.937, 24.473, 26.395, 28.862,
                 32.674, 37.47, 39.811]

plt.plot(salt_conc, np.array(x) * 60, label = 'x scaled by 60')
#plt.scatter(conc_Br, ion_cov, c = 'yellow', label = 'ion_cov/molecule_cov')
plt.scatter(conc_Br_isotherm, kink_pressure, c = 'green',
            label = 'transition pressure')
plt.xlabel('concentration(M)')
plt.ylabel('pressure(dynes)')
plt.legend()
plt.show()
