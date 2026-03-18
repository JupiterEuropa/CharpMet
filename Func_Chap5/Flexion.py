from Flexion_function import *

def M_Rd(fy = None, W = None, pl_el = None):
    print("Flexion Calc")
    if pl_el == None:
        pl_el = input("Plastic or elastic ?(1/0)")
    
    if pl_el == 1:
        M_rd = M_pl_Rd(fy= fy, W_pl= W)
    else:
        M_rd = M_el_Rd(fy= fy, W_el= W)
    return M_rd