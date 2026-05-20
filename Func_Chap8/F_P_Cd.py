def F_p_Cd():
    from constant import gamma_M
    A_s = float(input("A_s: ")) # mm^2
    f_ub = float(input("f_ub: ")) # MPa

    F_p = 0.7*A_s*f_ub/gamma_M[7] * 1e-3 # kN
    print("F_p,Cd = {:.4f}".format(F_p))
    return F_p