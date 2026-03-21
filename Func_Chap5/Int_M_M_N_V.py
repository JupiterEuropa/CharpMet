from math import sqrt
from constant import gamma_M
from .V_pl_Rd import V_pl_Rd
from .Aw import A_w_I_H
from .Traction import N_pl_Rd
from .Flexion_function import M_pl_Rd


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# Step 1 — shear-reduced moment resistances
# ---------------------------------------------------------------------------

def _M_V_Rd(rho, choice_section, fy, t_w, A_w, W_y_pl, W_z_pl):
    """Return (M_V_y_Rd, M_V_z_Rd) reduced for shear."""
    if rho == 0:
        M_V_y = W_y_pl * fy / gamma_M[0]
        M_V_z = W_z_pl * fy / gamma_M[0]
        return M_V_y, M_V_z

    if choice_section == 1:          # I/H: EC3 §6.2.8(3)
        M_V_y = (W_y_pl - rho * A_w**2 / (4 * t_w)) * fy / gamma_M[0]
    else:                            # Rect/Tube: reduced yield strength
        M_V_y = (1 - rho) * fy * W_y_pl / gamma_M[0]

    # Weak axis: always use reduced yield strength
    M_V_z = (1 - rho) * fy * W_z_pl / gamma_M[0]

    print(f"M_V,y,Rd = {M_V_y:.4g}")
    print(f"M_V,z,Rd = {M_V_z:.4g}")
    return M_V_y, M_V_z


# ---------------------------------------------------------------------------
# Step 2 — N-reduced moment resistances (based on reduced base M_V,Rd)
# ---------------------------------------------------------------------------

def _M_N_V_Rd(choice_section, n, a, a_w, a_f,
              M_V_y, M_V_z, N_Ed, A_w, fy, t_w):
    """Return (M_NV_y_Rd, M_NV_z_Rd) reduced for both shear and axial."""

    if choice_section == 1:          # I/H
        # Strong axis
        if n <= 0.25 and N_Ed <= 0.5 * A_w * fy / gamma_M[0]:
            M_NV_y = M_V_y
        else:
            M_NV_y = M_V_y * min((1 - n) / (1 - a/2), 1)

        # Weak axis
        if n <= 0.5 and N_Ed <= A_w * fy / gamma_M[0]:
            M_NV_z = M_V_z
        elif n <= a:
            M_NV_z = M_V_z
        else:
            M_NV_z = M_V_z * (1 - ((n - a) / (1 - a))**2)

    elif choice_section == 2:        # Tube
        M_NV_y = M_V_y * min((1 - n) / (1 - a_w/2), 1)
        M_NV_z = M_V_z * min((1 - n) / (1 - a_w/2), 1)

    else:                            # Rect
        M_NV_y = M_V_y * min((1 - n) / (1 - a_w/2), 1)
        M_NV_z = M_V_z * min((1 - n) / (1 - a_f/2), 1)

    print(f"M_NV,y,Rd = {M_NV_y:.4g}")
    print(f"M_NV,z,Rd = {M_NV_z:.4g}")
    return M_NV_y, M_NV_z


# ---------------------------------------------------------------------------
# Main function
# ---------------------------------------------------------------------------

def Int_M_M_N_V():
    """
    EC3 — M-M-N-V interaction (class 1/2 sections).

    Procedure:
      1. Compute V_pl,Rd and rho (shear reduction factor).
      2. Reduce M_pl,y,Rd and M_pl,z,Rd for shear → M_V,y/z,Rd.
      3. Further reduce for axial force N → M_NV,y/z,Rd.
      4. Check biaxial bending interaction:
             (M_y,Ed / M_NV,y,Rd)^α + (M_z,Ed / M_NV,z,Rd)^β ≤ 1
         or solve for the unknown moment if one is zero.
    """
    print("Int M-M-N-V")

    # --- Applied forces ---
    M_y_Ed = abs(float(input("M_y_Ed (0=tbd): ")))
    M_z_Ed = abs(float(input("M_z_Ed (0=tbd): ")))
    N_Ed   = abs(float(input("N_Ed: ")))
    V_Ed   = abs(float(input("V_Ed: ")))

    if M_y_Ed == 0 and M_z_Ed == 0:
        print("Both moments = 0")
        return None

    fy = float(input("fy: "))

    # --- Section geometry ---
    choice_section = _ask_section_type()

    A   = float(input("A: "))
    t_w = float(input("t_w: "))
    b   = float(input("b: "))
    t_f = float(input("t_f: "))

    if choice_section == 1:          # I/H
        welded_rolled = input("Welded/Rolled (1/0): ") == "1"
        h_w = float(input("h_w: "))
        h   = None
    else:
        welded_rolled = None
        h_w = None
        h   = float(input("h: "))

    W_y_pl = float(input("W_y,pl: "))
    W_z_pl = float(input("W_z,pl: "))

    # --- V_pl,Rd ---
    known_V = input("V_pl,Rd known (1/0): ") == "1"
    if known_V:
        V_pl_rd = float(input("V_pl,Rd: "))
    else:
        V_pl_rd, _ = V_pl_Rd(t_w=t_w, fy=fy)

    # --- Step 1: shear reduction factor rho ---
    if V_Ed > V_pl_rd / 2:
        rho = (2 * V_Ed / V_pl_rd - 1) ** 2
        print(f"rho = {rho:.4g}")
    else:
        rho = 0.0
        print("V<=V_pl/2: rho=0")

    # --- Section properties ---
    A_w = A_w_I_H(A=A, b=b, t_f=t_f, t_w=t_w, h_w=h_w,
                  welded_rolled=welded_rolled)

    N_pl_rd = N_pl_Rd(A=A, fy=fy)
    n       = N_Ed / N_pl_rd
    a       = min(1 - 2*b*t_f / A, 0.5)     # web area ratio (I/H)
    a_w     = min(A_w / A, 0.5)              # for Tube / Rect strong axis
    a_f     = min(1 - 2*h*t_w / A, 0.5) if h else a  # Rect weak axis

    # --- Step 2: shear-reduced moment resistances ---
    M_V_y, M_V_z = _M_V_Rd(rho, choice_section, fy, t_w, A_w, W_y_pl, W_z_pl)

    # --- Step 3: N-reduced moment resistances ---
    M_NV_y, M_NV_z = _M_N_V_Rd(choice_section, n, a, a_w, a_f,
                                 M_V_y, M_V_z, N_Ed, A_w, fy, t_w)

    # --- Step 4: biaxial interaction exponents ---
    if choice_section == 1:
        alpha = 2
        beta  = max(1, 5*n)
    elif choice_section == 2:
        alpha, beta = 2, 2
    else:
        alpha = min(6, 1.66 / (1 - 1.13*n**2))
        beta  = alpha

    # --- Step 5: check or solve ---
    if M_y_Ed != 0 and M_z_Ed != 0:
        # Both known: unity check
        UC = (M_y_Ed / M_NV_y)**alpha + (M_z_Ed / M_NV_z)**beta
        print(f"UC = {UC:.4g}")
        if UC <= 1:
            print("OK")
        else:
            print("FAIL")
        return UC

    elif M_y_Ed == 0:
        M_y_Ed = (1 - (M_z_Ed / M_NV_z)**beta)**(1/alpha) * M_NV_y
        print(f"M_y,Ed,max = {M_y_Ed:.4g}")
        return M_y_Ed

    else:
        M_z_Ed = (1 - (M_y_Ed / M_NV_y)**alpha)**(1/beta) * M_NV_z
        print(f"M_z,Ed,max = {M_z_Ed:.4g}")
        return M_z_Ed