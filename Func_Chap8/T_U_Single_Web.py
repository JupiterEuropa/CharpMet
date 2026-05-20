MENU = [
    (1, "N_pl_Rd"),
    (2, "N_u_Rd")
]

def T_U_single_web():
    from Menu_Display import printMenu
    print("T U single web")
    choice = printMenu(MENU)

    if choice == 1:
        N_pl_Rd()
    elif choice == 2:
        N_u_Rd()

def N_u_Rd():
    from constant import gamma_M
    Anet = A_net() # mm^2
    fu = float(input("fu: ")) # MPa
    N_u_Rd = 0.9 * Anet * fu / gamma_M[2] * 1e-3 # kN
    print("N_u,Rd = {:.4f}".format(N_u_Rd))
    return N_u_Rd

def A_net():
    choice = int(input("T (0) or U (1)"))
    A1 = float(input("A1: ")) # mm^2
    A2 = float(input("A2: ")) # mm^2
    if choice == 0:
        A_net = A1 + A2/2
    elif choice == 1:
        A_net = A1 + A2
    print("A_net = {:.4f}".format(A_net))
    return A_net

def N_pl_Rd():
    from constant import gamma_M

    A = float(input("A: ")) # mm^2
    fy = float(input("fy: ")) # MPa

    N_pl_Rd = A*fy/gamma_M[0] * 1e-3 # kN
    print("N_pl,Rd = {:.4f}".format(N_pl_Rd))
    return N_pl_Rd