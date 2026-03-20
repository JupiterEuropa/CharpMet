from .Aeff_V_function import *
from constant import *
from .Aeff_V_calc import A_eff_V

def V_pl_Rd(A = None, b = None, t_f = None, t_w = None, 
            h = None, h_w = None, r = None, number_of_webs = None, 
             fy = None) :
    print("V_pl_rd calc")  
    print("Verification of veiling")
    
    if fy is None:
        fy = float(input("fy: "))
    if h_w is None:
        h_w = float(input("h_w: "))
    if t_w is None:
        t_w = float(input("t_w: "))

    if h_w/t_w >= 72*epsilon[fy]/eta(fy):
        print("Instability from shear")
        return None, None, None
    else:
        print("No, instability")
        area, choice = A_eff_V(A = A, b = b, t_f = t_f, t_w = t_w, h= h, h_w= h_w, r= r, number_of_webs= number_of_webs, choice= choice)
        holes = bool(input("Any holes in the web ? (1/0)"))
        if holes == 1:
            hole_diameter = float(input("Hole diameter: "))
            number_of_holes = int(input("Number of holes: "))
            hole_area = number_of_holes * (math.pi * (hole_diameter/2)**2)
            area = area - hole_area
            V_pl_rd = area*fy/math.sqrt(3)/gamma_M[2]
            print("V_pl,Rd =", V_pl_rd)
            return V_pl_rd, choice
        else:
            V_pl_rd = area*fy/math.sqrt(3)/gamma_M[0]
            print("V_pl,Rd =", V_pl_rd)
            return V_pl_rd, choice