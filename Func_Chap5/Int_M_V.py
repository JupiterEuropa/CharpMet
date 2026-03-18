from .V_pl_Rd import *
from constant import *
from Func_Chap5.Flexion_function import *

def Int_M_V():
    choice = None
    area = None
    print("Interaction M-V")
    V_Ed = float(input("V_Ed: "))
    fy = float(input("fy: "))
    t_w = float(input("t_w: "))
    print("Known V_Pl,Rd ? (1/0)")
    known_V = int(input("Choice: "))
    if known_V == 1:
        V_plRd = float(input("V_Pl,Rd: "))
    else:    
        V_plRd, area, choice = V_pl_Rd(t_w= t_w, fy= fy) #1-2 -> I/H bent strong axis
    
    
    if V_Ed > V_plRd/2:
        print("Shear limits moment")     
        rho = (2*V_Ed/V_plRd-1)**2

        if choice == None:
            print("Shear:")
            print("Choose:")
            print("0: General")
            print("1: I/H Rolled //")
            print("2: I/H W //")
        
        if not (choice  == 1 or choice == 2):
            print("General section")
            fyr = (1 - rho)*fy
            print("Reduced fy (fyr) =", fyr)
            plastic_elastic = int(input("Plastic or elastic? (1/0)"))
            if plastic_elastic == 1:
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
        else:
            print("I/H section")
            
            if area == None and choice == 1:
                print("Rolled I/H")
                area = Rolled_I_H_Shear_Parallel_Web()
            else:
                print("Welded I/H")
                area = Welded_I_H_Shear_Parallel_Web()
            
            W_pl = float(input("W_pl: "))
            

            M_V_y_rd = (W_pl-rho*area**2/4/t_w)*fy/gamma_M[0]
            print("M_V,y,Rd =", M_V_y_rd)
            return M_V_y_rd
                
    else:
        print("No interraction M-V")
        plastic_elastic = int(input("Plastic or elastic? (1/0)"))
        if plastic_elastic == 1:
            M_pl_rd = M_pl_Rd(fy= fy)
            print("M_pl_Rd= ", M_pl_rd)
            return M_pl_rd
        else:
            M_el_rd = M_el_Rd(fy= fy)
            print("M_el_Rd= ", M_el_rd)
            return M_el_rd