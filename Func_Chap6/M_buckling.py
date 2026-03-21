from math import sqrt
from constant import gamma_M, epsilon
from .L_fl import Lfl

_ALPHA = {0: 0.13, 1: 0.21, 2: 0.34, 3: 0.49, 4: 0.76}

def _alpha() -> float:
    """EC3 Table 6.2 — buckling curve imperfection factor."""
    print("Buckling curve (!!S460!!)")
    print("0: a0  1: a")
    print("2: b   3: c  4: d")
    while True:
        try:
            choice = int(input("Choice (0-4): "))
            if choice in _ALPHA:
                alpha = _ALPHA[choice]
                print(f"alpha = {alpha}")
                return alpha
        except ValueError:
            pass
        print("Enter 0-4")


def N_b_Rd():
    print("N_b,Rd Calc")
    fy = float(input("fy: "))
    A  = float(input("A: "))
    I  = float(input("I: "))

    L_fl = Lfl(I=I)
    a    = _alpha()

    i          = sqrt(I / A)                  # radius of gyration
    lambda_1   = 93.9 * epsilon[fy]
    lmbda      = L_fl / i                     # slenderness
    lambda_red = lmbda / lambda_1

    phi = (1 + a * (lambda_red - 0.2) + lambda_red**2) / 2
    khi = min(1.0, 1 / (phi + sqrt(phi**2 - lambda_red**2)))

    print(f"lambda_red = {lambda_red:.4g}")
    print(f"phi = {phi:.4g}")
    print(f"khi = {khi:.4g}")

    N_b_rd = khi * A * fy / gamma_M[1]
    print(f"N_b,Rd = {N_b_rd:.4g}")
    return N_b_rd