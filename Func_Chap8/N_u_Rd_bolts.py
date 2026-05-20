def N_u_Rd_bolted():
    from constant import gamma_M, lerp
    
    number_of_bolts = int(input("Number of bolts: "))
    d0 = float(input("d0: "))
    t = float(input("t: "))
    fu = float(input("fu: "))
    
    if number_of_bolts == 1:
        e2 = float(input("e2: "))
        N_u_Rd = 2 * (e2 - 0.5* d0) * t * fu /gamma_M[2] * 1e-3 # kN
    elif number_of_bolts == 2:
        A = float(input("A: "))
        A_net = A - d0 * t
        p1 = float(input("p1: "))
        if p1 <= 2.5 * d0:
            beta_2 = 0.4
        elif p1 >= 5 * d0:
            beta_2 = 0.7
        else:
            beta_2 = lerp(p1, 2.5 * d0, 5 * d0, 0.4, 0.7)
        
        N_u_Rd = beta_2 * A_net * fu / gamma_M[2] * 1e-3 # kN
    else:
        A = float(input("A: "))
        A_net = A - d0 * t
        p1 = float(input("p1: "))
        if p1 <= 2.5 * d0:
            beta_3 = 0.5
        elif p1 >= 5 * d0:
            beta_3 = 0.7
        else:
            beta_3 = lerp(p1, 2.5 * d0, 5 * d0, 0.5, 0.7)

        N_u_Rd = beta_3 * A_net * fu / gamma_M[2] * 1e-3 # kN

    print("N_u,Rd = {:.4f}".format(N_u_Rd))

    return N_u_Rd
    