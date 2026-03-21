from .Int_M_N_function import (
    Int_M_N_I_y_y_cl1_cl2,
    Int_M_N_I_z_z_cl1_cl2,
    Int_M_N_Rect_Tube_y_y_cl1_cl2,
    Int_M_N_Rect_Tube_z_z_cl1_cl2,
)
from .Int_M_M_N_function import Int_M_M_N_cl3

def Int_M_N(A=None, A_w=None, fy=None, b=None, t_f=None, N_Ed=None,
            choice_section=None, choice_class=None, choice_flex=None,
            t_w=None, h_w=None, h=None, welded_rolled=None):

    print("Int M-N Calc")

    if choice_class is None:
        choice_class = int(input("Section class: "))

    if choice_section is None:
        print("Section type:")
        print("1: I/H")
        print("2: Rect/Tube")
        choice_section = int(input("Choice: "))

    if choice_flex is None:
        print("Bending axis:")
        print("1: Strong (y-y)")
        print("2: Weak  (z-z)")
        choice_flex = int(input("Choice: "))

    kw = dict(A=A, A_w=A_w, b=b, t_f=t_f, t_w=t_w, h_w=h_w,
              welded_rolled=welded_rolled, fy=fy, N_Ed=N_Ed)

    if choice_class in (1, 2):
        if choice_section == 1 and choice_flex == 1:
            return Int_M_N_I_y_y_cl1_cl2(**kw)
        elif choice_section == 1 and choice_flex == 2:
            return Int_M_N_I_z_z_cl1_cl2(**kw)
        elif choice_section == 2 and choice_flex == 1:
            return Int_M_N_Rect_Tube_y_y_cl1_cl2(A=A, A_w=A_w, b=b, t_f=t_f, fy=fy, N_Ed=N_Ed)
        elif choice_section == 2 and choice_flex == 2:
            return Int_M_N_Rect_Tube_z_z_cl1_cl2(A=A, A_w=A_w, b=b, t_w=t_w, h=h, fy=fy, N_Ed=N_Ed)
    else:
        return Int_M_M_N_cl3(mode_MN=True)
