from constant import gamma_M
from .Traction import N_pl_Rd
from .Flexion_function import M_pl_Rd
from .Aw import A_w_I_H
from math import sqrt

def Int_M_N_I_y_y_cl1_cl2(A=None, A_w=None, b=None, t_f=None, t_w=None,
                           h_w=None, welded_rolled=None, fy=None, N_Ed=None):
    print("Int M-N I/H y-y")
    if A   is None: A   = float(input("A: "))
    if b   is None: b   = float(input("b: "))
    if t_f is None: t_f = float(input("t_f: "))
    if fy  is None: fy  = float(input("fy: "))

    while True:        
        N_Ed = float(input("N_Ed (0=tbd): "))
        M_N_Rd = float(input("M_N,y,Rd (0=tbd): "))
        if N_Ed == 0 and M_N_Rd == 0:
            print("Both = 0")            
            continue
        else: break

    A_w     = A_w_I_H(A=A, A_w=A_w, b=b, t_f=t_f, t_w=t_w,
                      h_w=h_w, welded_rolled=welded_rolled)
    N_pl_rd = N_pl_Rd(A=A, fy=fy)
    n       = N_Ed / N_pl_rd
    a       = min(1 - 2*b*t_f / A, 0.5)
    M_pl_rd = M_pl_Rd(fy=fy)

    if N_Ed == 0:
        N_Ed = -N_pl_rd * (M_N_Rd / (M_pl_rd * (1 - a/2)) - 1)
        print("N_Ed = {:.4g}".format(N_Ed))
        return N_Ed
    elif n > 0.25 or N_Ed > 0.5 * A_w * fy / gamma_M[0]:
        M_N_Rd = M_pl_rd * min((1 - n) / (1 - a/2), 1)
        print("M_N,Rd = {:.4g}".format(M_N_Rd))
        return M_N_Rd
    else:
        print("No M-N interaction")
        print("M_pl,Rd = {:.4g}".format(M_pl_rd))
        return M_pl_rd


def Int_M_N_I_z_z_cl1_cl2(A=None, A_w=None, b=None, t_f=None, t_w=None,
                           h_w=None, welded_rolled=None, fy=None, N_Ed=None):
    print("Int M-N I/H z-z")
    if A   is None: A   = float(input("A: "))
    if b   is None: b   = float(input("b: "))
    if t_f is None: t_f = float(input("t_f: "))
    if fy  is None: fy  = float(input("fy: "))
    
    while True:        
        N_Ed = float(input("N_Ed (0=tbd): "))
        M_N_Rd = float(input("M_N,z,Rd (0=tbd): "))
        if N_Ed == 0 and M_N_Rd == 0:
            print("Both = 0")            
            continue
        else: break

    A_w     = A_w_I_H(A=A, A_w=A_w, b=b, t_f=t_f, t_w=t_w,
                      h_w=h_w, welded_rolled=welded_rolled)
    N_pl_rd = N_pl_Rd(A=A, fy=fy)
    n       = N_Ed / N_pl_rd
    a       = min(1 - 2*b*t_f / A, 0.5)
    M_pl_rd = M_pl_Rd(fy=fy)

    if (n > 0.5 or N_Ed > A_w * fy / gamma_M[0]) and M_N_Rd == 0:
        if n <= a:
            print("n<=a: M_N,Rd = {:.4g}".format(M_pl_rd))
            return M_pl_rd
        else:
            M_N_Rd = M_pl_rd * min((1 - ((n - a) / (1 - a))**2), 1)
            print("M_N,Rd = {:.4g}".format(M_N_Rd))
            return M_N_Rd
    elif N_Ed == 0:
        n = sqrt(1- M_N_Rd/M_pl_rd) * (1 - a) + a
        N_Ed = n * N_pl_rd
        print("N_Ed = {:.4g}".format(N_Ed))
        print("n = {:.4f}".format(n))
        print("a = {:.4f}".format(a))
        return N_Ed
    else:
        print("No M-N interaction")
        print("M_pl,Rd = {:.4g}".format(M_pl_rd))
        return M_pl_rd


def Int_M_N_Rect_Tube_y_y_cl1_cl2(A=None, A_w=None, b=None, t_f=None,
                                   fy=None, N_Ed=None):
    print("Int M-N Rect/Tube y-y")
    if A   is None: A   = float(input("A: "))
    if A_w is None: A_w = float(input("A_w: "))
    if b   is None: b   = float(input("b: "))
    if t_f is None: t_f = float(input("t_f: "))
    if fy  is None: fy  = float(input("fy: "))
    
    while True:
        N_Ed = float(input("N_Ed (0=tbd): "))
        M_N_Rd = float(input("M_N,y,Rd (0=tbd): "))
        if N_Ed == 0 and M_N_Rd == 0:
            print("Both = 0")            
            continue
        else: break


    N_pl_rd = N_pl_Rd(A=A, fy=fy)
    M_pl_rd = M_pl_Rd(fy=fy)
    n       = N_Ed / N_pl_rd
    a_w     = min(1 - 2*b*t_f / A, 0.5)
    if M_N_Rd == 0:
        M_N_Rd  = M_pl_rd * min((1 - n) / (1 - a_w/2), 1)
        print("M_N,y,Rd = {:.4g}".format(M_N_Rd))
        return M_N_Rd
    else:
        n = 1 - (M_N_Rd / M_pl_rd) * (1 - a_w/2)
        N_Ed = n * N_pl_rd
        print("N_Ed = {:.4g}".format(N_Ed))
        return N_Ed
    


def Int_M_N_Rect_Tube_z_z_cl1_cl2(A=None, A_w=None, b=None, t_w=None,
                                   h=None, fy=None, N_Ed=None):
    print("Int M-N Rect/Tube z-z")
    if A   is None: A   = float(input("A: "))
    if A_w is None: A_w = float(input("A_w: "))
    if b   is None: b   = float(input("b: "))
    if t_w is None: t_w = float(input("t_w: "))
    if fy  is None: fy  = float(input("fy: "))
    while True:
        N_Ed = float(input("N_Ed (0=tbd): "))
        M_N_Rd = float(input("M_N,z,Rd (0=tbd): "))
        if N_Ed == 0 and M_N_Rd == 0:
            print("Both = 0")            
            continue
        else: break

    N_pl_rd = N_pl_Rd(A=A, fy=fy)
    M_pl_rd = M_pl_Rd(fy=fy)
    n       = N_Ed / N_pl_rd
    a_f     = min(1 - 2*h*t_w / A, 0.5)
    if M_N_Rd == 0:        
        M_N_Rd  = M_pl_rd * min((1 - n) / (1 - a_f/2), 1)
        print("M_N,z,Rd = {:.4g}".format(M_N_Rd))
        return M_N_Rd
    else:
        n = 1 - (M_N_Rd / M_pl_rd) * (1 - a_f/2)
        N_Ed = n * N_pl_rd
        print("N_Ed = {:.4g}".format(N_Ed))
        return N_Ed


def Int_M_N_cl3():
    print("Int M-N class 3")
    while True:
        N_Ed = float(input("N_Ed: (0=tbd)"))
        M_y_Ed = float(input("M_Ed: (0=tbd)"))
        
        if N_Ed == 0 and M_y_Ed == 0:
            print("M_Ed and N_Ed = 0")
        else:
            break

    A      = float(input("A: "))
    W_el_y = float(input("W_el: " ))
    fy     = float(input("fy: "))

    if N_Ed == 0:
        N_Ed = (fy/gamma_M[0] - M_y_Ed / W_el_y) * A
        print("N_Ed = {:.4g}".format(N_Ed))
        return N_Ed
    elif M_y_Ed == 0:
        M_y_Ed = (fy/gamma_M[0] - N_Ed / A) * W_el_y
        print("M_Ed = {:.4f}".format(M_y_Ed))
        return M_y_Ed
    else:
        test = N_Ed / A / (fy/gamma_M[0]) + M_y_Ed / W_el_y / (fy/gamma_M[0])
        if test > 1:
            print("Interaction failure: {:.4f} > 1".format(test))
        else:
            print("Interaction success: {:.4f} <= 1".format(test))
        return test