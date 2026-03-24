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


def _M_V_Rd_general(rho, fy, W):
    """Shear-reduced moment for general / weak-axis: fyr = (1-rho)*fy."""
    return (1 - rho) * fy * W / gamma_M[0]


def _M_NV_Rd_IH_yy(W_pl, rho, A_w, t_w, N_Ed, fy):
    """
    EC3 §5.9 exact formula for I/H strong axis under M-N-V.

    MNV,y,Rd = [Wpl - 1/(4tw) * (rho*Aw^2 + NEd^2/((1-rho)*(fy/gM0)^2))]
               * fy/gM0

    Valid only if NEd <= Aw * fyr / gM0  where fyr = (1-rho)*fy.
    """
    fyr    = (1 - rho) * fy
    gM0    = gamma_M[0]
    A_w_fyr = A_w * fyr / gM0

    if N_Ed > A_w_fyr:
        print("N_Ed > Aw*fyr/gM0")
        print("Formula not applicable")
        return None

    if rho == 0:
        # Simplifies to standard M-N formula base; caller handles N reduction
        term = rho * A_w**2
    else:
        term = rho * A_w**2 + N_Ed**2 / ((1 - rho) * (fy / gM0)**2)

    M_NV_Rd = (W_pl - term / (4 * t_w)) * fy / gM0
    return M_NV_Rd


def Int_M_M_N_V():
    """
    EC3 §5.9 — M-M-N-V interaction for class 1/2 sections.

    For I/H strong axis: exact §5.9 formula.
    For weak axis and other sections: two-step (shear then N reduction).
    """
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

    # --- rho ---
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
    a_w     = min(A_w / A, 0.5) if A_w else 0
    a_f     = min(1 - 2*h*t_w / A, 0.5) if h else a

    # --- Strong axis: exact §5.9 formula for I/H ---
    if choice_section == 1:
        M_NV_y = _M_NV_Rd_IH_yy(W_y_pl, rho, A_w, t_w, N_Ed, fy)
        if M_NV_y is None:
            return None
        # Weak axis: shear reduces fyr, then apply N reduction
        M_V_z  = _M_V_Rd_general(rho, fy, W_z_pl)
        if n <= 0.5 and N_Ed <= A_w * fy / gamma_M[0]:
            M_NV_z = M_V_z
        elif n <= a:
            M_NV_z = M_V_z
        else:
            M_NV_z = M_V_z * (1 - ((n - a) / (1 - a))**2)

    elif choice_section == 2:  # Tube
        M_V_y  = _M_V_Rd_general(rho, fy, W_y_pl)
        M_V_z  = _M_V_Rd_general(rho, fy, W_z_pl)
        M_NV_y = M_V_y * min((1 - n) / (1 - a_w/2), 1)
        M_NV_z = M_V_z * min((1 - n) / (1 - a_w/2), 1)

    else:  # Rect
        M_V_y  = _M_V_Rd_general(rho, fy, W_y_pl)
        M_V_z  = _M_V_Rd_general(rho, fy, W_z_pl)
        M_NV_y = M_V_y * min((1 - n) / (1 - a_w/2), 1)
        M_NV_z = M_V_z * min((1 - n) / (1 - a_f/2), 1)

    M_NV_y = min(M_NV_y, W_y_pl * fy / gamma_M[0])
    print("M_NV,y,Rd = {:.4g}".format(M_NV_y))
    print("M_NV,z,Rd = {:.4g}".format(M_NV_z))

    # --- Biaxial exponents ---
    if choice_section == 1:
        alpha = 2
        beta  = max(1, 5*n)
    elif choice_section == 2:
        alpha, beta = 2, 2
    else:
        alpha = min(6, 1.66 / (1 - 1.13*n**2))
        beta  = alpha

    # --- Check or solve ---
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