from constant import gamma_M

def N_c_Rd(A=None, fy=None):
    print("N_c_Rd Calc")
    if A  is None: A  = float(input("A: "))
    if fy is None: fy = float(input("fy: "))
    N_c_rd = A * fy / gamma_M[0]
    print(f"N_c_Rd = {N_c_rd:.4g}")
    return N_c_rd