from .KSig import k_sigma
from math import pi

def critical_sigma():
    print("critical_sigma")
    E  = 210000  # MPa
    nu = 0.3

    t = float(input("t: "))
    b = float(input("b: "))

    if t <= 0 or b <= 0:
        print("t, b > 0")
        return None

    ks = k_sigma()
    sigma_crit = ks * (pi**2 * E) / (12 * (1 - nu**2)) * (t/b)**2

    print(f"sigma_crit = {sigma_crit:.2f} MPa")
    return sigma_crit