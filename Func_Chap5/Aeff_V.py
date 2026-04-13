def A_eff_V(A=None, b=None, t_f=None, t_w=None,
            h=None, h_w=None, r=None, number_of_webs=None):

    MENU = [
        (1,  "IHR//"),
        (2,  "IHW//"),
        (3,  "IHR-T"),
        (4,  "IHW-T"),
        (5,  "UR//"),
        (6,  "TR//"),
        (7,  "R//"),
        (8,  "R-T"),
        (9,  "Tube"),
        (10, "Known"),
    ]

    print("Shear A Calc:")
    while True:
        for i in range(0, len(MENU), 2):
            k1, label1 = MENU[i]
            line = "{:2}: {}".format(k1, label1)
            if i + 1 < len(MENU):
                k2, label2 = MENU[i + 1]
                line += "  {:2}: {}".format(k2, label2)
            print(line)

        try:
            choice = int(input("Choice (1-10): "))
        except ValueError:
            print("Enter 1-10")
            continue

        from .Aeff_V_function import (
            Rolled_I_H_Shear_Parallel_Web,
            Welded_I_H_Shear_Parallel_Web,
            Rolled_I_H_Shear_Perpendicular_Web,
            Welded_I_H_Shear_Perpendicular_Web,
            Rolled_U_Shear_Parallel_Web,
            Rolled_T_Shear_Parallel_Web,
            Rolled_Rectangular_Shear_Parallel_Web,
            Rolled_Rectangular_Shear_Perpendicular_Web,
            Tube_Shear,
        )
        
        if choice == 1:
            return Rolled_I_H_Shear_Parallel_Web(A=A, h=h, b=b, t_f=t_f, t_w=t_w, r=r), choice
        elif choice == 2:
            return Welded_I_H_Shear_Parallel_Web(h_w=h_w, t_w=t_w, number_of_webs=number_of_webs), choice
        elif choice == 3:
            return Rolled_I_H_Shear_Perpendicular_Web(b=b, t_f=t_f, t_w=t_w, r=r), choice
        elif choice == 4:
            return Welded_I_H_Shear_Perpendicular_Web(A=A, h_w=h_w, t_w=t_w, number_of_webs=number_of_webs), choice
        elif choice == 5:
            return Rolled_U_Shear_Parallel_Web(A=A, b=b, t_f=t_f, t_w=t_w, r=r), choice
        elif choice == 6:
            return Rolled_T_Shear_Parallel_Web(A=A, b=b, t_f=t_f), choice
        elif choice == 7:
            return Rolled_Rectangular_Shear_Parallel_Web(A=A, h=h, b=b), choice
        elif choice == 8:
            return Rolled_Rectangular_Shear_Perpendicular_Web(A=A, h=h, b=b), choice
        elif choice == 9:
            return Tube_Shear(A=A), choice
        elif choice == 10:
            return float(input("Known Aeff: ")), choice
        print("Enter 1-10")