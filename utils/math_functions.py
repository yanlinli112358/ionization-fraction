import numpy as np

#get ionization fraction from Gouy Chapman model
def get_x(salt_conc, pH, pKa):
    #g = LHS of eq(4) in 'Salt promotes protonation'
    def g(salt_conc, pH):
        return np.sqrt(salt_conc + 10 ** (-pH))
    #f = RHS of eq(4)
    def f(pH, pKa, x):
        temp = (np.log10((1 - x) / x) - pH + pKa) / 0.87
        return 134 * x / (20 * np.sinh(temp))
    #objective = abs(LHS-RHS)
    def objective(x):
        return abs(g(salt_conc, pH) - f(pH, pKa, x))
    #res is the solutions that minimize the difference b/w LHS and RHS
    from scipy.optimize import minimize_scalar
    res = minimize_scalar(objective, bounds=(0, 1), method='bounded')

    return res.x

#given a list of salt_concentration, compute ionization fraction
def ionization_frac(salt_conc, pH, pKa):
    ion_frac = []
    for c in salt_conc:
        x = get_x(c, pH, pKa)
        ion_frac.append(x)
    return ion_frac

