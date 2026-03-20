from constant import *

def N_pl_Rd(A = None, fy = None):
    print("Traction calc")
    if A is None:
        A = float(input("A: "))
    if fy is None:
        fy = float(input("fy: "))
    
    
    
    
    N_pl_rd = A * fy / gamma_M[0]

    print("N_pl_Rd= ", N_pl_rd)
    return N_pl_rd

def N_u_Rd(b = None, t = None, fu = None, s = None, p = None, d0 = None):
    if b is None:
        b = float(input("b: "))
    if t is None:
        t = float(input("t: "))
    if fu is None:
        fu = float(input("fu: "))
    if s is None:
        s = float(input("s: "))
    if p is None:
        p = float(input("p: "))
    if d0 is None:
        d0 = float(input("d0: "))
        
    choice = int(input("Section 1-1 or 2-2 ?(1/2)"))
    if choice == 1:
        A_net = b * t - d0 * t 
    else:   
        A_net = b * t - (2 * d0 *t - s**2 * t /4 /p) 
    N_u_rd = 0.9 * A_net * fu / gamma_M[2]

    print("N_u_Rd = ", N_u_rd)
    return N_u_rd