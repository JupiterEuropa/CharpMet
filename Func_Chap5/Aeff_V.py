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

def A_eff_V(A=None, b=None, t_f=None, t_w=None,
            h=None, h_w=None, r=None, number_of_webs=None):

    MENU = [
        (1,  "IHR//",    lambda: Rolled_I_H_Shear_Parallel_Web(A=A, h=h, b=b, t_f=t_f, t_w=t_w, r=r)),
        (2,  "IHW//",    lambda: Welded_I_H_Shear_Parallel_Web(h_w=h_w, t_w=t_w, number_of_webs=number_of_webs)),
        (3,  "IHR-T",    lambda: Rolled_I_H_Shear_Perpendicular_Web(b=b, t_f=t_f, t_w=t_w, r=r)),
        (4,  "IHW-T",    lambda: Welded_I_H_Shear_Perpendicular_Web(A=A, h_w=h_w, t_w=t_w, number_of_webs=number_of_webs)),
        (5,  "UR//",     lambda: Rolled_U_Shear_Parallel_Web(A=A, b=b, t_f=t_f, t_w=t_w, r=r)),
        (6,  "TR//",     lambda: Rolled_T_Shear_Parallel_Web(A=A, b=b, t_f=t_f)),
        (7,  "R//",      lambda: Rolled_Rectangular_Shear_Parallel_Web(A=A, h=h, b=b)),
        (8,  "R-T",      lambda: Rolled_Rectangular_Shear_Perpendicular_Web(A=A, h=h, b=b)),
        (9,  "Tube",     lambda: Tube_Shear(A=A)),
        (10, "Known",    lambda: float(input("Known Aeff: "))),
    ]

    print("Shear A Calc:")
    while True:
        for i in range(0, len(MENU), 2):
            k1, label1, _ = MENU[i]
            line = "{:2}: {}".format(k1, label1)
            if i + 1 < len(MENU):
                k2, label2, _ = MENU[i + 1]
                line += "  {:2}: {}".format(k2, label2)
            print(line)

        try:
            choice = int(input("Choice (1-10): "))
        except ValueError:
            print("Enter 1-10")
            continue

        fn = None
        for k, _, f in MENU:
            if k == choice:
                fn = f
                break
        
        if fn:
            return fn(), choice
        print("Enter 1-10")