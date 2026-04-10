from .Traction import N_pl_Rd
from .Int_M_N import Int_M_N
from .Aw import A_w_I_H
from constant import gamma_M

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
        print("M_y,Ed = {:.4g}".format(M_y_Ed))
    else:
        M_z_Ed = (1 - (M_y_Ed / M_N_y_rd)**alpha)**(1/beta) * M_N_z_rd
        print("M_z,Ed = {:.4g}".format(M_z_Ed))


def Int_M_M_N_cl3():
    print("Int M-M-N cl3")

    while True:
        M_y_Ed = float(input("M_y_Ed: (0=tbd)"))
        M_z_Ed = float(input("M_z_Ed: (0=tbd)"))
        N_Ed = float(input("N_Ed: (0=tbd)"))

        if (M_y_Ed == 0 and M_z_Ed == 0) or N_Ed == 0:
            print("Moments or N_Ed = 0")
            continue
        else: break

    A      = float(input("A: "))
    W_el_y = float(input("W_el_y: "))
    W_el_z = float(input("W_el_z: "))
    fy     = float(input("fy: "))

    if M_y_Ed == 0:
        M_y_Ed = (fy/gamma_M[0]*1e-6 - N_Ed / A * 1e-3 - M_z_Ed / W_el_z) * W_el_y
        print("M_y,Ed = {:.4g}".format(M_y_Ed))
    elif M_z_Ed == 0:
        M_z_Ed = (fy/gamma_M[0]*1e-6 - N_Ed / A * 1e-3 - M_y_Ed / W_el_y) * W_el_z
        print("M_z,Ed = {:.4g}".format(M_z_Ed))
    else:
        N_Ed = A * (fy/gamma_M[0]*1e-3 - M_y_Ed / W_el_y * 1e3 - M_z_Ed / W_el_z * 1e3)
        print("N_Ed = {:.4g}".format(N_Ed))
