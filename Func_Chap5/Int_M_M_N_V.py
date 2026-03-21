from math import sqrt
from constant import gamma_M
from .V_pl_Rd import V_pl_Rd
from .Aw import A_w_I_H
from .Traction import N_pl_Rd
from .Flexion_function import M_pl_Rd


def _ask_section_type():
    print("Section type:")
    print("1: I/H")
    print("2: Tube")
    print("3: Rect")
    while True:
        try:
            c = int(input("Choice: "))
            if c in (1, 2, 3):
                return c
        except ValueError:
            pass
        print("Enter 1-3")


def _ask_plastic():
    return input("Plastic/Elastic (1/0): ") == "1"


def _M_V_Rd(rho, choice_section, fy, t_w, A_w, W_y_pl, W_z_pl):
    if rho == 0:
        M_V_y = W_y_pl * fy / gamma_M[0]
        M_V_z = W_z_pl * fy / gamma_M[0]
        return M_V_y, M_V_z

    if choice_section == 1:
        M_V_y = (W_y_pl - rho * A_w**2 / (4 * t_w)) * fy / gamma_M[0]
    else:
        M_V_y = (1 - rho) * fy * W_y_pl / gamma_M[0]

    M_V_z = (1 - rho) * fy * W_z_pl / gamma_M[0]

    print("M_V,y,Rd = {:.4g}".format(M_V_y))
    print("M_V,z,Rd = {:.4g}".format(M_V_z))
    return M_V_y, M_V_z


def _M_N_V_Rd(choice_section, n, a, a_w, a_f,
              M_V_y, M_V_z, N_Ed, A_w, fy, t_w):
    if choice_section == 1:
        if n <= 0.25 and N_Ed <= 0.5 * A_w * fy / gamma_M[0]:
            M_NV_y = M_V_y
        else:
            M_NV_y = M_V_y * min((1 - n) / (1 - a/2), 1)

        if n <= 0.5 and N_Ed <= A_w * fy / gamma_M[0]:
            M_NV_z = M_V_z
        elif n <= a:
            M_NV_z = M_V_z
        else:
            M_NV_z = M_V_z * (1 - ((n - a) / (1 - a))**2)

    elif choice_section == 2:
        M_NV_y = M_V_y * min((1 - n) / (1 - a_w/2), 1)
        M_NV_z = M_V_z * min((1 - n) / (1 - a_w/2), 1)

    else:
        M_NV_y = M_V_y * min((1 - n) / (1 - a_w/2), 1)
        M_NV_z = M_V_z * min((1 - n) / (1 - a_f/2), 1)

    print("M_NV,y,Rd = {:.4g}".format(M_NV_y))
    print("M_NV,z,Rd = {:.4g}".format(M_NV_z))
    return M_NV_y, M_NV_z


def Int_M_M_N_V():
    print("Int M-M-N-V")

    M_y_Ed = abs(float(input("M_y_Ed (0=tbd): ")))
    M_z_Ed = abs(float(input("M_z_Ed (0=tbd): ")))
    N_Ed   = abs(float(input("N_Ed: ")))
    V_Ed   = abs(float(input("V_Ed: ")))

    if M_y_Ed == 0 and M_z_Ed == 0:
        print("Both moments = 0")
        return None

    fy = float(input("fy: "))

    choice_section = _ask_section_type()

    A   = float(input("A: "))
    t_w = float(input("t_w: "))
    b   = float(input("b: "))
    t_f = float(input("t_f: "))

    if choice_section == 1:
        welded_rolled = input("Welded/Rolled (1/0): ") == "1"
        h_w = float(input("h_w: "))
        h   = None
    else:
        welded_rolled = None
        h_w = None
        h   = float(input("h: "))

    W_y_pl = float(input("W_y,pl: "))
    W_z_pl = float(input("W_z,pl: "))

    known_V = input("V_pl,Rd known (1/0): ") == "1"
    if known_V:
        V_pl_rd = float(input("V_pl,Rd: "))
    else:
        V_pl_rd, _ = V_pl_Rd(t_w=t_w, fy=fy)

    if V_Ed > V_pl_rd / 2:
        rho = (2 * V_Ed / V_pl_rd - 1) ** 2
        print("rho = {:.4g}".format(rho))
    else:
        rho = 0.0
        print("V<=V_pl/2: rho=0")

    A_w = A_w_I_H(A=A, b=b, t_f=t_f, t_w=t_w, h_w=h_w,
                  welded_rolled=welded_rolled)

    N_pl_rd = N_pl_Rd(A=A, fy=fy)
    n       = N_Ed / N_pl_rd
    a       = min(1 - 2*b*t_f / A, 0.5)
    a_w     = min(A_w / A, 0.5)
    a_f     = min(1 - 2*h*t_w / A, 0.5) if h else a

    M_V_y, M_V_z = _M_V_Rd(rho, choice_section, fy, t_w, A_w, W_y_pl, W_z_pl)

    M_NV_y, M_NV_z = _M_N_V_Rd(choice_section, n, a, a_w, a_f,
                                M_V_y, M_V_z, N_Ed, A_w, fy, t_w)

    if choice_section == 1:
        alpha = 2
        beta  = max(1, 5*n)
    elif choice_section == 2:
        alpha, beta = 2, 2
    else:
        alpha = min(6, 1.66 / (1 - 1.13*n**2))
        beta  = alpha

    if M_y_Ed != 0 and M_z_Ed != 0:
        UC = (M_y_Ed / M_NV_y)**alpha + (M_z_Ed / M_NV_z)**beta
        print("UC = {:.4g}".format(UC))
        print("OK" if UC <= 1 else "FAIL")
        return UC
    elif M_y_Ed == 0:
        M_y_Ed = (1 - (M_z_Ed / M_NV_z)**beta)**(1/alpha) * M_NV_y
        print("M_y,Ed,max = {:.4g}".format(M_y_Ed))
        return M_y_Ed
    else:
        M_z_Ed = (1 - (M_y_Ed / M_NV_y)**alpha)**(1/beta) * M_NV_z
        print("M_z,Ed,max = {:.4g}".format(M_z_Ed))
        return M_z_Ed
