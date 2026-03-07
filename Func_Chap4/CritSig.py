#Working fine
from .KSig import k_sigma
from math import *

def critical_sigma():
    print("critical_sigma")
    E = 210000 # MPa
    nu = 0.3
    
    t = float(input("t :"))
    b = float(input("b :"))

    k_sigma_value = k_sigma()
    if t <= 0 or b <= 0:
        print("t and b must be greater than 0.")
        return None
    sigma_crit = k_sigma_value * (pi**2 * E) / (12 * (1 - nu**2)) * (t/b)**2
    print("sigma_crit = ")
    print(sigma_crit, "MPa") #Broke the line for better readability
    return sigma_crit