from constant import *

def N_pl_Rd(A = None, b = None, t = None, fy = None, fu = None, s = None, p = None, d0 = None):
    print("Traction calc")
    if A == None:
        A = float(input("A: "))
    # if b == None:
    #     b = float(input("b: "))
    # if t == None:
    #     t = float(input("t: "))
    if fy == None:
        fy = float(input("fy: "))
    # if fu == None:
    #     fu = float(input("fu: "))
    # if s == None:
    #     s = float(input("s: "))
    # if p == None:
    #     p = float(input("p: "))
    # if d0 == None:
    #     d0 = float(input("d0: "))
    
    # if choice == 1:
    #     A_net = b * t - d0 * t 
    # else:   
    #     A_net = b * t - (2 * d0 *t - s**2 * t /4 /p) 
    # N_u_Rd = 0.9 * A_net * fu / gamma_M[2]
    
    N_pl_Rd = A * fy / gamma_M[0]

    return N_pl_Rd #, N_u_Rd