from math import sqrt
from .KSig import k_sigma

def cantilevered_compressed_wall(epsilon: float):
    c = float(input("c :"))
    t = float(input("t :"))

    if c <= 0 or t <= 0:
        print("c,t > 0")
        return None
    
    c_over_t = c/t

    if c_over_t <= 9*epsilon:
        print("Section is class 1")
        return 1
    elif c_over_t <= 10*epsilon:
        print("Section is class 2")
        return 2
    elif c_over_t <= 14*epsilon:
        print("Section is class 3")
        return 3
    else:
        print("Section is class 4")
        return 4

def cantilevered_compressed_flexed_wall(epsilon: float):
    c = float(input("c :"))
    t = float(input("t :"))
    alpha = float(input("alpha :"))
    extremity_stress = bool(input("ext compressed(1/0):"))

    if c <= 0 or t <= 0 or alpha <= 0:
        print("c,t,α > 0")
        return None
    
    c_over_t = c/t

    if extremity_stress and c_over_t <= 9*epsilon/alpha:
        print("Section is class 1")
        return 1
    elif extremity_stress and c_over_t <= 10*epsilon/alpha:
        print("Section is class 2")
        return 2
    elif not extremity_stress and c_over_t <= 9*epsilon/alpha/sqrt(alpha):
        print("Section is class 1")
        return 1
    elif not extremity_stress and c_over_t <= 10*epsilon/alpha/sqrt(alpha):
        print("Section is class 2")
        return 2
    else:
        k_sigma_value = k_sigma()
        if c_over_t <= 21*epsilon*sqrt(k_sigma_value):
            print("Section is class 3")
            return 3
        else:
            print("Section is class 4")
            return 4

def internal_flexed_wall (epsilon: float):
    c = float(input("c :"))
    t = float(input("t :"))

    if c <= 0 or t <= 0:
        print("c,t > 0")
        return None
    
    
    c_over_t = c/t

    if c_over_t <= 72*epsilon:
        print("Section is class 1")
        return 1
    elif c_over_t <= 83*epsilon:
        print("Section is class 2")
        return 2
    elif c_over_t <= 124*epsilon:
        print("Section is class 3")
        return 3
    else:
        print("Section is class 4")
        return 4
    
def internal_compressed_wall (epsilon: float):
    c = float(input("c :"))
    t = float(input("t :"))

    if c <= 0 or t <= 0:
        print("c,t > 0")
        return None
    
    c_over_t = c/t

    if c_over_t <= 33*epsilon:
        print("Section is class 1")
        return 1
    elif c_over_t <= 38*epsilon:
        print("Section is class 2")
        return 2
    elif c_over_t <= 42*epsilon:
        print("Section is class 3")
        return 3
    else:
        print("Section is class 4")
        return 4

def internal_compressed_flexed_wall (epsilon: float):
    c = float(input("c :"))
    t = float(input("t :"))
    alpha = float(input("alpha :"))

    if c <= 0 or t <= 0 or alpha <= 0:
        print("c,t,α > 0")
        return None
    
    c_over_t = c/t

    if alpha > 0.5:
        if c_over_t <= 396*epsilon/(13*alpha-1):
            print("Section is class 1")
            return 1
        elif c_over_t <= 456*epsilon/(13*alpha-1):
            print("Section is class 2")
            return 2
    elif alpha <= 0.5:
        if c_over_t <= 36*epsilon/alpha:
            print("Section is class 1")
            return 1
        elif c_over_t <= 41.5*epsilon/alpha:
            print("Section is class 2")
            return 2
    
    # Only ask for sigma values if class 3 or 4 is possible
    sigma1 = float(input("sigma1: "))
    sigma2 = float(input("sigma2: "))
    EPSILON = sigma2/sigma1

    if EPSILON > -1 and c_over_t <= 42*epsilon/(0.67+0.33*EPSILON):
        print("Section is class 3")
        return 3
    elif EPSILON <= -1 and c_over_t <= 62*epsilon*(1-EPSILON)*sqrt(-EPSILON):
        print("Section is class 3")
        return 3
    else:
        print("Section is class 4")
        return 4

