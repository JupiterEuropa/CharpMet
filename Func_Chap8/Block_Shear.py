def Block_shear():
    from constant import gamma_M
    from math import sqrt
    A_nv = float(input("A_nv: "))
    A_nt = float(input("A_nt: "))
    fy = float(input("fy: "))
    fu = float(input("fu: "))
    choice = int(input("Eccentric load (1/0):"))
    if choice == 0:
        V_eff = A_nt * fu / gamma_M[2] + A_nv * fy / gamma_M[0] / sqrt(3)
    else:
        V_eff = 0.5 * A_nt * fu / gamma_M[2] + A_nv * fy / gamma_M[0] / sqrt(3)

    print("V_eff = {:.4f} kN".format(V_eff))
    return V_eff