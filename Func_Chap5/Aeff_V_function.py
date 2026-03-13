import math

def Rolled_I_H_Shear_Parallel_Web():
    print("I/H, Shear // Web")
    print("Enter dimensions:")
    h = float(input("Height (h): "))
    b = float(input("Flange width (b): "))
    t_w = float(input("Web thickness (t_w): "))
    t_f = float(input("Flange thickness (t_f): "))
    r = float(input("Root radius (r): "))
    A = float(input("Area (A): "))
    return print("Shear Area :", max(A - 2*b*t_f + (t_w + 2*r)*t_f, (h-2*t_f)*t_w))

def Welded_I_H_Shear_Parallel_Web():
    print("I/H Welded,")
    print("Shear // Web")
    number_of_webs = int(input("Number of webs: "))
    A_w = 0
    for i in range(number_of_webs):
        print("Web", i+1)
        h_w = float(input("Height (h_w): "))
        t_w = float(input("Thickness: "))
        A_w = A_w + h_w * t_w
    return print("Shear Area :", A_w)

def Rolled_I_H_Shear_Perpendicular_Web():
    print("I/H, Shear ⟂ Web")
    print("Enter dimensions:")
    b = float(input("Flange (b): "))
    t_f = float(input("Flange thick: "))
    t_w = float(input("Web thick: "))
    r = float(input("Radius (r): "))
    return print("Shear Area :", 2*b*t_f + (t_w + r)*t_w)

def Welded_I_H_Shear_Perpendicular_Web():
    print("I/H Welded,")
    print("Shear ⟂ Web")
    number_of_webs = int(input("Number of webs: "))
    A_w = 0
    for i in range(number_of_webs):
        print("Web", i+1)
        t_w = float(input("Thickness: "))
        A_w = A_w + t_w * t_w

    A = float(input("Area (A): "))
    return print("Shear Area :", A - A_w)

def Rolled_U_Shear_Parallel_Web():
    print("U, Shear // Web")
    print("Enter dimensions:")
    b = float(input("Flange (b): "))
    t_w = float(input("Web thick: "))
    t_f = float(input("Flange thick: "))
    r = float(input("Radius (r): "))
    A = float(input("Area (A): "))
    return print("Shear Area :", A - 2*b*t_f + (t_w +r)*t_f)

def Rolled_T_Shear_Parallel_Web():
    print("T, Shear // Web")
    print("Enter dimensions:")
    b = float(input("Flange (b): "))
    t_f = float(input("Flange thick: "))
    A = float(input("Area (A): "))
    return print("Shear Area :", 0.9*(A - b*t_f))

def Rolled_Rectangular_Shear_Parallel_Web():
    print("Rectangular,")
    print("Shear // Web")
    print("Enter dimensions:")
    b = float(input("Width (b): "))
    h = float(input("Height (h): "))
    A = float(input("Area (A): "))
    return print("Shear Area :", A*h/(b+h))

def Rolled_Rectangular_Shear_Perpendicular_Web():
    print("Rectangular,")
    print("Shear ⟂ Web")
    print("Enter dimensions:")
    b = float(input("Width (b): "))
    h = float(input("Height (h): "))
    A = float(input("Area (A): "))
    return print("Shear Area :", A*b/(b+h))

def Tube_Shear():
    print("Tube, Shear")
    print("Enter dimensions:")
    A = float(input("Area (A): "))
    return print("Shear Area :", 2*A/math.pi)