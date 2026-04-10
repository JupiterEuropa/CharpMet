from constant import gamma_M

def N_pl_Rd(A=None, fy=None):
    print("N_pl,Rd Calc")
    if A  is None: A  = float(input("A: "))
    if fy is None: fy = float(input("fy: "))
    N_pl_rd = A * fy / gamma_M[0]/1000
    print("N_pl,Rd = {:.4g}".format(N_pl_rd))
    return N_pl_rd

def N_u_Rd(b=None, t=None, fu=None, s=None, p=None, d0=None):
    print("N_u,Rd Calc")
    try:
        choice = int(input("Section 1-1/2-2 (1/2): "))
    except ValueError:
        print("Enter 1 or 2")
        return None
    
    if fu is None: fu = float(input("fu: "))
    if b  is None: b  = float(input("b: "))
    if d0 is None: d0 = float(input("d0: "))    
    if t  is None: t  = float(input("t: "))

    if choice == 1:
        A_net = (b - d0) * t
    elif choice == 2:
        if s  is None: s  = float(input("s: "))
        if p  is None: p  = float(input("p: "))
        A_net = (b - 2*d0 + s**2 / (4*p)) * t    

    N_u_rd = 0.9 * A_net * fu / gamma_M[2]/1000
    print("N_u,Rd = {:.4g}".format(N_u_rd))
    return N_u_rd
