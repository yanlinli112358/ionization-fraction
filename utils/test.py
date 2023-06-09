import numpy as np
import matplotlib.pyplot as plt

from math_functions import ionization_frac
salt_conc = np.linspace(0, 1e-3, 100)
pH = 5.7
pKa = 10.5
x = ionization_frac(salt_conc, pH, pKa)

conc_Br = 1e-3 * np.array([0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.75])
ion_cov = [0.1077, 0.1278, 0.3162, 0.3285, 0.3329,
           0.3613, 0.3791, 0.3967, 0.5624, 0.6013]

plt.plot(salt_conc, x, label = 'model')
plt.scatter(conc_Br, ion_cov, c = 'orange', label = 'XF_fitting')
plt.xlabel('Bromine concentration(M)')
plt.ylabel('ionization fraction')
plt.title('pH = 5.7, pKa = 10.5')
plt.savefig('/Users/rachel/APS_beamtrips/2023feb/ionization fraction.jpeg')

plt.show()

