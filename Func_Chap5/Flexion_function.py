from constant import gamma_M

def M_pl_Rd(fy=None, W_pl=None):
    print("M_pl_Rd Calc")
    if fy   is None: fy   = float(input("fy: "))
    if W_pl is None: W_pl = float(input("W_pl: "))
    M_pl_rd = W_pl * fy / gamma_M[0]
    print(f"M_pl,Rd = {M_pl_rd:.4g}")
    return M_pl_rd

def M_el_Rd(fy=None, W_el=None):
    print("M_el_Rd Calc")
    if fy   is None: fy   = float(input("fy: "))
    if W_el is None: W_el = float(input("W_el: "))
    M_el_rd = W_el * fy / gamma_M[0]
    print(f"M_el,Rd = {M_el_rd:.4g}")
    return M_el_rd