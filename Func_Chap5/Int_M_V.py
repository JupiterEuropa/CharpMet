from .Aeff_V_function import *
def Int_M_V():
    print("Shear Calc:")
    print("Choose:")
    print("1-2: I/H (R/W) //")
    print("3-4: I/H (R/W) T")
    print("5-6: U/T //")
    print("7-8: Rect // T")
    print("9: Tube")
    choice = int(input("Choice: "))

    if choice == 1:
        Rolled_I_H_Shear_Parallel_Web()
    elif choice == 2:
        Welded_I_H_Shear_Parallel_Web()
    elif choice == 3:
        Rolled_I_H_Shear_Perpendicular_Web()
    elif choice == 4:
        Welded_I_H_Shear_Perpendicular_Web()
    elif choice == 5:
        Rolled_U_Shear_Parallel_Web()
    elif choice == 6:
        Rolled_T_Shear_Parallel_Web()
    elif choice == 7:
        Rolled_Rectangular_Shear_Parallel_Web()
    elif choice == 8:
        Rolled_Rectangular_Shear_Perpendicular_Web()
    elif choice == 9:
        Tube_Shear()
    else:
        print("Invalid choice.")
        print("Enter 1-9.")