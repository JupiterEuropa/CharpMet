from .V_pl_Rd import *
from constant import *
from Func_Chap5.Flexion_function import *
from Aw import A_w_I_H

def Int_M_V():
    choice = None
    print("Interaction M-V")
    V_Ed = float(input("V_Ed: (tbd:0)"))
    fy = float(input("fy: "))
    t_w = float(input("t_w: "))
    known_V = bool(input("Known V_Pl,Rd ? (1/0)"))
    if known_V :
        V_plRd = float(input("V_Pl,Rd: "))
    else:    
        V_plRd, choice = V_pl_Rd(t_w= t_w, fy= fy) #1-2 -> I/H bent strong axis
    
    
    if V_Ed > V_plRd/2 or V_Ed == 0:
        if V_Ed != 0:
            print("Shear limits moment")     
            rho = (2*V_Ed/V_plRd-1)**2

            if choice is None:
                print("Shear:")
                print("Choose:")
                print("0: General")
                print("1: I y-y")
                print("2: H y-y")
                choice = int(input("Choice: "))
            
            if choice not in (1, 2):
                print("General section")
                fyr = (1 - rho)*fy
                print("Reduced fy (fyr) =", fyr)
                plastic_elastic = bool(input("Plastic or elastic? (1/0)"))
                if plastic_elastic:
                    print("Plastic section")
                    W_pl = float(input("W_pl: "))
                    M_V_pl_Rd = fyr*W_pl/gamma_M[0]
                    print("M_V_pl,Rd =", M_V_pl_Rd)
                    return M_V_pl_Rd
                else:
                    print("Elastic section")
                    W_el = float(input("W_el: "))
                    M_V_el_Rd = fyr*W_el/gamma_M[0]
                    print("M_V_el,Rd =", M_V_el_Rd)
                    return M_V_el_Rd

            else :
                print("I/H section")
                A_w = A_w_I_H(t_w=t_w)         
                W_pl = float(input("W_y_pl: "))
                M_V_y_rd = (W_pl - rho * A_w**2/4/t_w)*fy/gamma_M[0]
                print("M_V,y,Rd =", M_V_y_rd)
                return M_V_y_rd
            
        else:
            print("Determining V_Ed")
            if choice is None:
                print("Shear:")
                print("Choose:")
                print("0: General")
                print("1: I y-y")
                print("2: H y-y")
                choice = int(input("Choice: "))
            
            if choice not in (1, 2):
                print("General section")

            else :
                print("I/H section")
                
    else:
        print("No interraction M-V")
        plastic_elastic = bool(input("Plastic or elastic? (1/0)"))
        if plastic_elastic:
            M_pl_rd = M_pl_Rd(fy= fy)
            print("M_pl,Rd= ", M_pl_rd)
            return M_pl_rd
        else:
            M_el_rd = M_el_Rd(fy= fy)
            print("M_el,Rd= ", M_el_rd)
            return M_el_rd