MENU = [
    (1, "N_pl_Rd"),
    (2, "N_u_Rd")
]


def Corner_single_web_welded():
    from Menu_Display import printMenu
    print("Corner welded single web")
    choice = printMenu(MENU)

    if choice == 1:
        N_pl_Rd()
    elif choice == 2:
        N_u_Rd_welded()


def N_u_Rd_welded():
    from constant import gamma_M
    A_eff = float(input("A_eff: "))
    fu = float(input("fu: "))
    N_u_Rd = 0.9 * A_eff * fu / gamma_M[2] * 1e-3 # kN
    print("N_u,Rd = {:.4f}".format(N_u_Rd))
    return N_u_Rd

def N_pl_Rd():
    from constant import gamma_M

    A = float(input("A: ")) # mm^2
    fy = float(input("fy: ")) # MPa

    N_pl_Rd = A*fy/gamma_M[0] * 1e-3 # kN
    print("N_pl,Rd = {:.4f}".format(N_pl_Rd))
    return N_pl_Rd