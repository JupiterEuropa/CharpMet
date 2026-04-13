from math import pi
from constant import E

def critical_sigma():
    print("critical_sigma")
    from .KSig import k_sigma
    
    nu = 0.3

    t = float(input("t: "))
    b = float(input("b: "))

    if t <= 0 or b <= 0:
        print("t, b > 0")
        return None

    ks = k_sigma()
    sigma_crit = ks * (pi**2 * E) / (12 * (1 - nu**2)) * (t/b)**2

    print("sigma_crit = {:.4g} MPa".format(sigma_crit))
    return sigma_crit
