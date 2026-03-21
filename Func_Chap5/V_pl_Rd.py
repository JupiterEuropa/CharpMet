from math import sqrt, pi
from constant import gamma_M, epsilon, eta
from .Aeff_V_calc import A_eff_V

def V_pl_Rd(A=None, b=None, t_f=None, t_w=None,
            h=None, h_w=None, r=None, number_of_webs=None, fy=None):
    print("V_pl,Rd Calc")

    if fy  is None: fy  = float(input("fy: "))
    if h_w is None: h_w = float(input("h_w: "))
    if t_w is None: t_w = float(input("t_w: "))

    if h_w / t_w >= 72 * epsilon[fy] / eta(fy):
        print("Instability: EN1993-1-5")
        return None, None

    print("No instability")
    area, choice = A_eff_V(A=A, b=b, t_f=t_f, t_w=t_w,
                           h=h, h_w=h_w, r=r, number_of_webs=number_of_webs)

    if input("Holes in web (1/0): ") == "1":
        d0 = float(input("Hole diameter: "))
        n  = int(input("Num holes: "))
        area -= n * pi * (d0/2)**2
        V_pl_rd = area * fy / sqrt(3) / gamma_M[2]
    else:
        V_pl_rd = area * fy / sqrt(3) / gamma_M[0]

    print("V_pl,Rd = {:.4g}".format(V_pl_rd))
    return V_pl_rd, choice