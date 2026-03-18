import math

def Rolled_I_H_Shear_Parallel_Web(A = None, h = None, b = None, t_f = None, t_w = None, r = None):
    print("I/H, Shear // Web")
    if A == None:
        A = float(input("Area (A): "))
    if h == None:
        h = float(input("h: "))
    if b == None:
        b = float(input("b: "))
    if t_f == None:
        t_f = float(input("t_f: "))
    if t_w == None:
        t_w = float(input("t_w: "))
    if r == None:
        r = float(input("r: "))
    return print("Shear Area :", max(A - 2*b*t_f + (t_w + 2*r)*t_f, (h-2*t_f)*t_w))

def Welded_I_H_Shear_Parallel_Web(h_w = None, t_w = None, number_of_webs = None):
    A_w = 0
    print("I/H Welded,")
    print("Shear // Web")
    if h_w == None or t_w == None or number_of_webs == None:
        number_of_webs = int(input("Number of webs: "))
        
        for i in range(number_of_webs):
            print("Web", i+1)
            h_w = float(input("Height (h_w): "))
            t_w = float(input("Thickness: "))
            A_w = A_w + h_w * t_w
    else:
        A_w = A_w + h_w * t_w
    return print("Shear Area :", A_w)

def Rolled_I_H_Shear_Perpendicular_Web(b = None, t_f = None, t_w = None, r = None):
    print("I/H, Shear T Web")
    print("Enter dimensions:")
    if b == None:
        b = float(input("Flange (b): "))
    if t_f == None:
        t_f = float(input("Flange thick: "))
    if t_w == None:
        t_w = float(input("Web thick: "))
    if r == None:
        r = float(input("Radius (r): "))
    return print("Shear Area :", 2*b*t_f + (t_w + r)*t_w)

def Welded_I_H_Shear_Perpendicular_Web(A = None, h_w = None, t_w = None, number_of_webs = None):
    A_w = 0
    print("I/H Welded,")
    print("Shear T Web")
    if A == None or h_w == None or t_w == None or number_of_webs == None:
        A = float(input("Area (A): "))
        number_of_webs = int(input("Number of webs: "))
        
        for i in range(number_of_webs):
            print("Web", i+1)
            h_w = float(input("Height (h_w): "))
            t_w = float(input("Thickness: "))
            A_w = A_w + t_w * h_w
    else:
        A_w = t_w * h_w
    
    return print("Shear Area :", A - A_w)

def Rolled_U_Shear_Parallel_Web(A = None, b = None, t_f = None, t_w = None, r = None):
    print("U, Shear // Web")
    print("Enter dimensions:")
    if A == None:
        A = float(input("Area (A): "))
    if b == None:
        b = float(input("Flange (b): "))
    if t_f == None:
        t_f = float(input("Flange thick: "))
    if t_w == None:
        t_w = float(input("Web thick: "))
    if r == None:
        r = float(input("Radius (r): "))
    return print("Shear Area :", A - 2*b*t_f + (t_w +r)*t_f)

def Rolled_T_Shear_Parallel_Web(A = None, b = None, t_f = None):
    print("T, Shear // Web")
    print("Enter dimensions:")
    if A == None:
        A = float(input("Area (A): "))
    if b == None:
        b = float(input("Flange (b): "))
    if t_f == None:
        t_f = float(input("Flange thick: "))
    return print("Shear Area :", 0.9*(A - b*t_f))

def Rolled_Rectangular_Shear_Parallel_Web(A = None, h = None, b = None):
    print("Rectangular,")
    print("Shear // Web")
    print("Enter dimensions:")
    if A == None:
        A = float(input("Area (A): "))
    if h == None:
        h = float(input("Height (h): "))
    if b == None:
        b = float(input("Width (b): "))
    return print("Shear Area :", A*h/(b+h))

def Rolled_Rectangular_Shear_Perpendicular_Web(A = None, h = None, b = None):
    print("Rectangular,")
    print("Shear T Web")
    print("Enter dimensions:")
    if A == None:
        A = float(input("Area (A): "))
    if h == None:
        h = float(input("Height (h): "))
    if b == None:
        b = float(input("Width (b): "))
    return print("Shear Area :", A*b/(b+h))

def Tube_Shear(A = None):
    print("Tube, Shear")
    print("Enter dimensions:")
    if A == None:
        A = float(input("Area (A): "))
    return print("Shear Area :", 2*A/math.pi)