from .Traction import N_pl_Rd
from .Int_M_N import Int_M_N
from .Aw import A_w_I_H

def Int_M_M_N_cl1_cl2():
    print("Int M-M-N cl1/cl2")

    flag = True
    while flag:
        M_y_Ed = abs(float(input("M_y_Ed (0=tbd): ")))
        M_z_Ed = abs(float(input("M_z_Ed (0=tbd): ")))
        N_Ed   = abs(float(input("N_Ed: ")))
        flag = (M_y_Ed == 0 and M_z_Ed == 0) or N_Ed == 0
        if flag:
            print("Moments or N_Ed = 0")

    A  = float(input("A: "))
    fy = float(input("fy: "))
    N_pl_rd = N_pl_Rd(A=A, fy=fy)

    while True:
        print("Section type:")
        print("1: I/H")
        print("2: Tube")
        print("3: Rect")
        try:
            choice_section = int(input("Choice: "))
        except ValueError:
            print("Enter 1-3")
            continue
        if choice_section in (1, 2, 3):
            break
        print("Enter 1-3")

    t_w = float(input("t_w: "))
    b   = float(input("b: "))
    t_f = float(input("t_f: "))

    if choice_section == 1:
        welded_rolled = input("Welded/Rolled (1/0): ") == "1"
        h_w = float(input("h_w: "))
        h   = None
        A_w = A_w_I_H(A=A, b=b, t_f=t_f, t_w=t_w, h_w=h_w, welded_rolled=welded_rolled)
    else:
        welded_rolled = None
        h_w = None
        h   = float(input("h: "))
        A_w = None

    M_N_y_rd = Int_M_N(A=A, A_w=A_w, fy=fy, b=b, t_f=t_f, N_Ed=N_Ed,
                       choice_section=choice_section, choice_class=1,
                       choice_flex=1, t_w=t_w, h_w=h_w, h=h,
                       welded_rolled=welded_rolled)
    M_N_z_rd = Int_M_N(A=A, A_w=A_w, fy=fy, b=b, t_f=t_f, N_Ed=N_Ed,
                       choice_section=choice_section, choice_class=1,
                       choice_flex=2, t_w=t_w, h_w=h_w, h=h,
                       welded_rolled=welded_rolled)

    n = N_Ed / N_pl_rd

    if choice_section == 1:
        alpha = 2
        beta  = max(1, 5*n)
    elif choice_section == 2:
        alpha, beta = 2, 2
    else:
        alpha = min(6, 1.66 / (1 - 1.13*n**2))
        beta  = alpha

    if M_y_Ed == 0:
        M_y_Ed = (1 - (M_z_Ed / M_N_z_rd)**beta)**(1/alpha) * M_N_y_rd
        print(f"M_y,Ed = {M_y_Ed:.4g}")
    else:
        M_z_Ed = (1 - (M_y_Ed / M_N_y_rd)**alpha)**(1/beta) * M_N_z_rd
        print(f"M_z,Ed = {M_z_Ed:.4g}")


def Int_M_M_N_cl3(mode_MM: bool = False, mode_MN: bool = False):
    """
    Shared class-3 interaction check.
    mode_MM=True : M-M only   (N_Ed = 0 implicitly)
    mode_MN=True : M-N only   (single bending axis)
    default      : full M-M-N
    """
    if mode_MM:
        print("Int M-M cl3")
    elif mode_MN:
        print("Int M-N cl3")
    else:
        print("Int M-M-N cl3")

    while True:
        N_Ed = 0.0 if mode_MM else float(input("N_Ed: "))

        if mode_MN:
            M_y_Ed = float(input("M_Ed: "))
            M_z_Ed = 0.0
        else:
            M_y_Ed = float(input("M_y_Ed: "))
            M_z_Ed = float(input("M_z_Ed: "))

        zeros = [N_Ed, M_y_Ed, M_z_Ed].count(0.0)
        if mode_MM and M_y_Ed == 0 and M_z_Ed == 0:
            print("Both moments = 0")
        elif mode_MN and N_Ed == 0 and M_y_Ed == 0:
            print("M_Ed and N_Ed = 0")
        elif not mode_MM and not mode_MN and zeros >= 2:
            print("2+ vars are 0")
        else:
            break

    A     = 1.0 if mode_MM else float(input("A: "))
    W_el_y = float(input("W_el: " if mode_MN else "W_el_y: "))
    W_el_z = 1.0 if mode_MN else float(input("W_el_z: "))
    fy     = float(input("fy: "))

    if N_Ed == 0 and not mode_MM:
        N_Ed = (fy - M_z_Ed / W_el_z - M_y_Ed / W_el_y) * A
        print(f"N_Ed = {N_Ed:.4g}")
    elif M_y_Ed == 0:
        M_y_Ed = (fy - N_Ed / A - M_z_Ed / W_el_z) * W_el_y
        print(f"M_y,Ed = {M_y_Ed:.4g}")
    elif M_z_Ed == 0 and not mode_MN:
        M_z_Ed = (fy - N_Ed / A - M_y_Ed / W_el_y) * W_el_z
        print(f"M_z,Ed = {M_z_Ed:.4g}")