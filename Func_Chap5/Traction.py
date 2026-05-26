from constant import gamma_M
MENU = [
    (1, "N_pl,Rd"),
    (2, "N_u,Rd"),
]
def Traction():
    from Menu_Display import printMenu
    choice = printMenu(MENU)
    if choice == 1:
        N_pl_Rd()
    elif choice == 2:
        N_u_Rd()

    return

def N_pl_Rd(A=None, fy=None):
    print("N_pl,Rd Calc")
    if A  is None: A  = float(input("A: "))
    if fy is None: fy = float(input("fy: "))
    N_pl_rd = A * fy / gamma_M[0]/1000
    print("N_pl,Rd = {:.4g}".format(N_pl_rd))
    return N_pl_rd

def N_u_Rd(b=None, t=None, fu=None, s=None, p=None, d0=None, nbr_holes_1=None, nbr_diag=None):
    print("N_u,Rd Calc")
    try:
        choice = int(input("2-2 present ? (1/0): "))
    except ValueError:
        print("Enter 0 or 1")
        return None
    A_net = [0, 0]
    if fu is None: fu = float(input("fu: "))
    if b  is None: b  = float(input("b: "))
    if d0 is None: d0 = float(input("d0: "))    
    if t  is None: t  = float(input("t: "))
    if nbr_holes_1 is None: nbr_holes_1 = int(input("Nbr holes 1-1: "))
    
    d0_1 = d0 * nbr_holes_1
    A_net[0] = (b - d0_1) * t
    print("A_net,1 = {:.4g}".format(A_net[0]))
    if choice == 1:
        A_net[1] = b*t
        if nbr_diag is None: nbr_diag = int(input("Nbr stagger :"))
        A_net[1] -= (nbr_diag + 1) * d0 * t
        for i in range(nbr_diag):
             if s is None: s  = float(input("s_{}: ".format(i+1)))
             if p is None: p  = float(input("p_{}: ".format(i+1)))
             A_net[1] += s**2*t/4/p 
             s = None
             p = None
        
        print("A_net,2 = {:.4g}".format(A_net[1]))
    
    N_u_rd = 0.9 * min(A_net) * fu / gamma_M[2]/1000
    print("N_u,Rd = {:.4g}".format(N_u_rd))
    return N_u_rd