from constant import gamma_M

def N_c_Rd(A = None, fy = None):
    print("N_c_Rd Calc")
    if A == None:
        A = float(input("A: "))
    if fy == None:
        fy = float(input("fy: "))
    
    N_c_rd = A * fy / gamma_M[0]
    print("N_c_rd= ", N_c_rd)
    return N_c_rd