from .Aeff_V_function import *
def V_pl_Rd():
    print("Shear Calc:")
    print("Choose:")
    print("1-2: I/H (R/W) //")
    print("3-4: I/H (R/W) T")
    print("5-6: U/T //")
    print("7-8: Rect // T")
    print("9: Tube")
    choice = int(input("Choice: "))

    if choice == 1:
        area=Rolled_I_H_Shear_Parallel_Web()
    elif choice == 2:
        area=Welded_I_H_Shear_Parallel_Web()
    elif choice == 3:
        area=Rolled_I_H_Shear_Perpendicular_Web()
    elif choice == 4:
        area=Welded_I_H_Shear_Perpendicular_Web()
    elif choice == 5:
        area=Rolled_U_Shear_Parallel_Web()
    elif choice == 6:
        area=Rolled_T_Shear_Parallel_Web()
    elif choice == 7:
        area=Rolled_Rectangular_Shear_Parallel_Web()
    elif choice == 8:
        area=Rolled_Rectangular_Shear_Perpendicular_Web()
    elif choice == 9:
        area=Tube_Shear()
    else:
        print("Invalid")
        print("Enter 1-9")
    
    fy = float(input("fy: "))

    return print("V_pl,Rd =", area*fy/math.sqrt(3))