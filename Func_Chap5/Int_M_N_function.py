from constant import gamma_M
from .Traction import *
from Func_Chap5.Flexion_function import *

def Int_M_N_I_y_y_cl1_cl2(A = None, A_w = None, b = None, t_f = None, t_w = None, 
                    h = None, h_w = None, r = None, number_of_webs = None, 
                    fy = None, N_Ed = None):
    print("Int M-N Calc, I/H y-y")
    if A == None:
        A = float(input("A: "))
    if A_w == None:
        A_w = float(input("A_w: "))
    if b == None:
        b = float(input("b: "))
    if t_f == None:
        t_f = float(input("t_f: "))
    if fy == None:
        fy = float(input("fy: "))
    if N_Ed == None:
        N_Ed = float(input("N_Ed: "))


    N_pl_rd = N_pl_Rd(A= A, fy= fy)
    n = N_Ed/N_pl_rd
    a = min(1 - 2 * b * t_f /A, 0.5)
    
    M_pl_rd = M_pl_Rd(fy= fy)

    if n > 0.25 or N_Ed > 0.5 * A_w * fy / gamma_M[0]:
        print("N limits M_y")
        M_N_Rd = M_pl_rd * min((1 - n)/(1- a/2), 1)
        print("M_N_Rd= ", M_N_Rd)
        return M_N_Rd
    else:
        print("No interraction M-N")
        print("M_pl_Rd= ", M_pl_rd)
        return M_pl_rd

def Int_M_N_I_z_z_cl1_cl2(A = None, A_w = None, b = None, t_f = None, t_w = None, 
                    h = None, h_w = None, r = None, number_of_webs = None, 
                    fy = None, N_Ed = None):
    
    print("Int M-N Calc, I/H z-z")
    if A == None:
        A = float(input("A: "))
    if A_w == None:
        A_w = float(input("A_w: "))
    if b == None:
        b = float(input("b: "))
    if t_f == None:
        t_f = float(input("t_f: "))
    if fy == None:
        fy = float(input("fy: "))
    if N_Ed == None:
        N_Ed = float(input("N_Ed: "))

    N_pl_rd = N_pl_Rd(A= A, fy= fy)
    n = N_Ed/N_pl_rd
    a = min(1 - 2 * b * t_f /A, 0.5)

    M_pl_rd = M_pl_Rd(fy= fy)
    
    if n > 0.5 or N_Ed > A_w * fy / gamma_M[0]:
        print("N limits M_z")
        if n <= a:
            print("Edge case, n <= a")
            print("M_N_Rd= ", M_pl_rd)
            return M_pl_rd
        else: 
            M_N_Rd = M_pl_rd * (1-((n - a)/(1 - a))**2)
            print("M_N_Rd= ", M_N_Rd)
            return M_N_Rd
    else:
        print("No interraction M-N")
        print("M_pl_Rd= ", M_pl_rd)
        return M_pl_rd
    
def Int_M_N_Rect_y_y_cl1_cl2(A = None, A_w = None, b = None, t_f = None, t_w = None, 
                    h = None, h_w = None, r = None, number_of_webs = None, 
                    fy = None, N_Ed = None):
    
    print("Int M-N Calc, Rect y-y")
    if A == None:
        A = float(input("A: "))
    if A_w == None:
        A_w = float(input("A_w: "))
    if b == None:
        b = float(input("b: "))
    if t_f == None:
        t_f = float(input("t_f/t: "))
    if fy == None:
        fy = float(input("fy: "))
    if N_Ed == None:
        N_Ed = float(input("N_Ed: "))


    N_pl_rd = N_pl_Rd(A= A, fy= fy)
    M_pl_rd = M_pl_Rd(fy= fy)  
    
    n = N_Ed/N_pl_rd

    a_w = min(1 - 2*b*t_f/A, 0.5)
      

    M_N_Rd = M_pl_rd * min((1 - n)/(1 - a_w/2),1)
    print("M_N_y_Rd= ", M_N_Rd)
    return M_N_Rd

def Int_M_N_Rect_z_z_cl1_cl2(A = None, A_w = None, b = None, t_w = None, 
                    h = None, h_w = None, r = None, number_of_webs = None, 
                    fy = None, N_Ed = None):
    
    print("Int M-N Calc, Rect z-z")
    if A == None:
        A = float(input("A: "))
    if A_w == None:
        A_w = float(input("A_w: "))
    if b == None:
        b = float(input("b: "))
    if t_w == None:
        t_w = float(input("t_w/t: "))
    if fy == None:
        fy = float(input("fy: "))
    if N_Ed == None:
        N_Ed = float(input("N_Ed: "))


    N_pl_rd = N_pl_Rd(A= A, fy= fy)
    M_pl_rd = M_pl_Rd(fy= fy)  
    
    n = N_Ed/N_pl_rd

    a_f = min(1 - 2*h*t_w/A, 0.5)

    M_N_Rd = M_pl_rd * min((1 - n)/(1 - a_f/2),1)
    print("M_N_z_Rd= ", M_N_Rd)
    return M_N_Rd
