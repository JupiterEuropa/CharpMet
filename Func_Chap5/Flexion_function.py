from constant import gamma_M

def M_pl_Rd(fy=None, W_pl=None):
    print("M_pl,Rd Calc")
    if fy   is None: fy   = float(input("fy: "))
    if W_pl is None: W_pl = float(input("W_pl: "))
    M_pl_rd = W_pl * fy / gamma_M[0] * 1e-6
    print("M_pl,Rd = {:.4g}".format(M_pl_rd))
    return M_pl_rd

def M_el_Rd(fy=None, W_el=None):
    print("M_el,Rd Calc")
    if fy   is None: fy   = float(input("fy: "))
    if W_el is None: W_el = float(input("W_el: "))
    M_el_rd = W_el * fy / gamma_M[0] * 1e-6
    print("M_el,Rd = {:.4g}".format(M_el_rd))
    return M_el_rd
