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
        (1,  "I/H R // Web", lambda: Rolled_I_H_Shear_Parallel_Web(A=A, h=h, b=b, t_f=t_f, t_w=t_w, r=r)),
        (2,  "I/H W // Web", lambda: Welded_I_H_Shear_Parallel_Web(h_w=h_w, t_w=t_w, number_of_webs=number_of_webs)),
        (3,  "I/H R T Web",  lambda: Rolled_I_H_Shear_Perpendicular_Web(b=b, t_f=t_f, t_w=t_w, r=r)),
        (4,  "I/H W T Web",  lambda: Welded_I_H_Shear_Perpendicular_Web(A=A, h_w=h_w, t_w=t_w, number_of_webs=number_of_webs)),
        (5,  "U R // Web",   lambda: Rolled_U_Shear_Parallel_Web(A=A, b=b, t_f=t_f, t_w=t_w, r=r)),
        (6,  "T R // Web",   lambda: Rolled_T_Shear_Parallel_Web(A=A, b=b, t_f=t_f)),
        (7,  "Rect // Web",  lambda: Rolled_Rectangular_Shear_Parallel_Web(A=A, h=h, b=b)),
        (8,  "Rect T Web",   lambda: Rolled_Rectangular_Shear_Perpendicular_Web(A=A, h=h, b=b)),
        (9,  "Tube",         lambda: Tube_Shear(A=A)),
        (10, "Known Aeff",   lambda: float(input("Known Aeff: "))),
    ]

    print("Shear A Calc:")
    while True:
        for k, label, _ in MENU:
            print("{:2}: {}".format(k, label))

        try:
            choice = int(input("Choice (1-10): "))
        except ValueError:
            print("Enter 1-10")
            continue

        fn = next((f for k, _, f in MENU if k == choice), None)
        if fn:
            return fn(), choice
        print("Enter 1-10")