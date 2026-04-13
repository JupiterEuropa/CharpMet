from math import sqrt
from constant import gamma_M, epsilon
from .L_fl import Lfl

_ALPHA = {0: 0.13, 1: 0.21, 2: 0.34, 3: 0.49, 4: 0.76}

def _alpha():
    print("Buckling curve")
    print("0:a0  1:a")
    print("2:b   3:c  4:d")
    while True:
        try:
            choice = int(input("Choice (0-4): "))
            if choice in _ALPHA:
                a = _ALPHA[choice]
                print("alpha = {:.4g}".format(a))
                return a
        except ValueError:
            print("Enter 0-4")
            pass
        


def N_b_Rd():
    print("N_b,Rd Calc")
    fy  = float(input("fy: "))
    A   = float(input("A: "))
    I   = float(input("I: "))
    N_Ed = float(input("N_Ed: "))

    if bool(input("L_fl known (1/0): ")):
        L_fl = float(input("L_fl: "))
    else:
        L_fl = Lfl(I=I)
    N_cr = 0  # computed below after L_fl is known

    from math import pi
    from constant import E
    N_cr = pi**2 * E * I / L_fl**2

    i          = sqrt(I / A)
    lambda_1   = 93.9 * epsilon[fy]
    lmbda      = L_fl / i
    lambda_red = lmbda / lambda_1

    # EC3 §6.3.1: no buckling check needed if conditions are met
    if lambda_red <= 0.2 or N_Ed / N_cr <= 0.04:
        print("No buckling check")
        N_b_rd = A * fy / gamma_M[1]
        print("N_b,Rd = {:.4g}".format(N_b_rd))
        return N_b_rd

    a   = _alpha()
    phi = (1 + a * (lambda_red - 0.2) + lambda_red**2) / 2
    khi = min(1.0, 1 / (phi + sqrt(phi**2 - lambda_red**2)))

    print("lambda = {:.4g}".format(lambda_red))
    print("phi = {:.4g}".format(phi))
    print("khi = {:.4g}".format(khi))

    N_b_rd = khi * A * fy / gamma_M[1]
    print("N_b,Rd = {:.4g}".format(N_b_rd))
    return N_b_rd