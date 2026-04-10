from .Flexion_function import M_pl_Rd, M_el_Rd

def M_Rd(fy=None, W=None, pl_el=None):
    print("Flexion Calc")
    if pl_el is None:
        pl_el = input("Pl/El(1/0): ") == "1"
    if pl_el:
        return M_pl_Rd(fy=fy, W_pl=W)
    else:
        return M_el_Rd(fy=fy, W_el=W)
