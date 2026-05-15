def N_u_Rd_welded():
    from constant import gamma_M
    A_eff = float(input("A_eff: "))
    fu = float(input("fu: "))
    N_u_Rd = 0.9 * A_eff * fu / gamma_M[2] * 1e-3 # kN
    print("N_u,Rd = {:.4f}".format(N_u_Rd))
    return N_u_Rd