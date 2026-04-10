from constant import gamma_M

def N_c_Rd(A=None, fy=None):
    print("N_c,Rd Calc")
    if A  is None: A  = float(input("A: "))
    if fy is None: fy = float(input("fy: "))
    N_c_rd = A * fy / gamma_M[0]/1000
    print("N_c,Rd = {:.4g}".format(N_c_rd))
    return N_c_rd
