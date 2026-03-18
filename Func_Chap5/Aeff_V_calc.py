from .Aeff_V_function import *


def A_eff_V(A = None, b = None, t_f = None, t_w = None, 
            h = None, h_w = None, r = None, number_of_webs = None):
    while True:
        print("Shear A Calc:")
        
        print("Choose:")
        print("1-2: I/H (R/W) //")
        print("3-4: I/H (R/W) T")
        print("5-6: U/T //")
        print("7-8: Rect // T")
        print("9-10: Tube/Known")
        choice = int(input("Choice: "))

        if choice == 1:
            area=Rolled_I_H_Shear_Parallel_Web(A= A, b= b, t_f= t_f, t_w= t_w, r= r)
            break
        elif choice == 2:
            area=Welded_I_H_Shear_Parallel_Web(h_w= h_w, t_w= t_w, number_of_webs= number_of_webs)
            break
        elif choice == 3:
            area=Rolled_I_H_Shear_Perpendicular_Web(b= b, t_f= t_f, t_w= t_w, r= r)
            break   
        elif choice == 4:
            area=Welded_I_H_Shear_Perpendicular_Web(A= A, h_w= h_w, t_w= t_w, number_of_webs= number_of_webs)
            break
        elif choice == 5:
            area=Rolled_U_Shear_Parallel_Web(A= A, b= b, t_f= t_f, t_w= t_w, r= r)
            break
        elif choice == 6:
            area=Rolled_T_Shear_Parallel_Web(A= A, b= b, t_f= t_f)
            break
        elif choice == 7:
            area=Rolled_Rectangular_Shear_Parallel_Web(A= A, h= h, b= b)
            break
        elif choice == 8:
            area=Rolled_Rectangular_Shear_Perpendicular_Web(A= A, h= h, b= b)
            break
        elif choice == 9:
            area=Tube_Shear(A= A)
            break
        elif choice == 10:
            area=float(input("Known Aeff: "))
            break
        else:
            print("Invalid")
            print("Enter 1-10")
            input("Any key to continue...")
            continue

    return area, choice