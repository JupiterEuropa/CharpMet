from math import pi

def Rolled_I_H_Shear_Parallel_Web(A=None, h=None, b=None, t_f=None, t_w=None, r=None):
    print("I/H Rolled // Web")
    if A   is None: A   = float(input("A: "))
    if h   is None: h   = float(input("h: "))
    if b   is None: b   = float(input("b: "))
    if t_f is None: t_f = float(input("t_f: "))
    if t_w is None: t_w = float(input("t_w: "))
    if r   is None: r   = float(input("r: "))
    A_V = max(A - 2*b*t_f + (t_w + 2*r)*t_f, (h - 2*t_f)*t_w)
    print("Shear A: {:.4g}".format(A_V))
    return A_V

def Welded_I_H_Shear_Parallel_Web(h_w=None, t_w=None, number_of_webs=None):
    print("I/H Welded // Web")
    A_w = 0
    if h_w is None or t_w is None or number_of_webs is None:
        number_of_webs = int(input("Num webs: "))
        for i in range(number_of_webs):
            print("Web {}".format(i + 1))
            h_w = float(input("h_w: "))
            t_w = float(input("t_w: "))
            A_w += h_w * t_w
    else:
        A_w = h_w * t_w
    print("Shear A: {:.4g}".format(A_w))
    return A_w

def Rolled_I_H_Shear_Perpendicular_Web(b=None, t_f=None, t_w=None, r=None):
    print("I/H Rolled T Web")
    if b   is None: b   = float(input("b: "))
    if t_f is None: t_f = float(input("t_f: "))
    if t_w is None: t_w = float(input("t_w: "))
    if r   is None: r   = float(input("r: "))
    A_V = 2*b*t_f + (t_w + r)*t_w
    print("Shear A: {:.4g}".format(A_V))
    return A_V

def Welded_I_H_Shear_Perpendicular_Web(A=None, h_w=None, t_w=None, number_of_webs=None):
    print("I/H Welded T Web")
    A_w = 0
    if A is None or h_w is None or t_w is None or number_of_webs is None:
        A              = float(input("A: "))
        number_of_webs = int(input("Num webs: "))
        for i in range(number_of_webs):
            print("Web {}".format(i + 1))
            h_w  = float(input("h_w: "))
            t_w  = float(input("t_w: "))
            A_w += h_w * t_w
    else:
        A_w = h_w * t_w
    A_V = A - A_w
    print("Shear A: {:.4g}".format(A_V))
    return A_V

def Rolled_U_Shear_Parallel_Web(A=None, b=None, t_f=None, t_w=None, r=None):
    print("U Rolled // Web")
    if A   is None: A   = float(input("A: "))
    if b   is None: b   = float(input("b: "))
    if t_f is None: t_f = float(input("t_f: "))
    if t_w is None: t_w = float(input("t_w: "))
    if r   is None: r   = float(input("r: "))
    A_V = A - 2*b*t_f + (t_w + r)*t_f
    print("Shear A: {:.4g}".format(A_V))
    return A_V

def Rolled_T_Shear_Parallel_Web(A=None, b=None, t_f=None):
    print("T Rolled // Web")
    if A   is None: A   = float(input("A: "))
    if b   is None: b   = float(input("b: "))
    if t_f is None: t_f = float(input("t_f: "))
    A_V = 0.9 * (A - b*t_f)
    print("Shear A: {:.4g}".format(A_V))
    return A_V

def Rolled_Rectangular_Shear_Parallel_Web(A=None, h=None, b=None):
    print("Rect // Web")
    if A is None: A = float(input("A: "))
    if h is None: h = float(input("h: "))
    if b is None: b = float(input("b: "))
    A_V = A * h / (b + h)
    print("Shear A: {:.4g}".format(A_V))
    return A_V

def Rolled_Rectangular_Shear_Perpendicular_Web(A=None, h=None, b=None):
    print("Rect T Web")
    if A is None: A = float(input("A: "))
    if h is None: h = float(input("h: "))
    if b is None: b = float(input("b: "))
    A_V = A * b / (b + h)
    print("Shear A: {:.4g}".format(A_V))
    return A_V

def Tube_Shear(A=None):
    print("Tube Shear")
    if A is None: A = float(input("A: "))
    A_V = 2 * A / pi
    print("Shear A: {:.4g}".format(A_V))
    return A_V
