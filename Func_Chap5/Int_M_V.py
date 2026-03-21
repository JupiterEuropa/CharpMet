from .V_pl_Rd import V_pl_Rd
from constant import gamma_M
from Func_Chap5.Flexion_function import M_pl_Rd, M_el_Rd
from Aw import A_w_I_H


def Int_M_V():
    """
    EC3 - Section 6.2.8 : Interaction M-V (Moment-Shear).

    Two modes:
      - Forward  : V_Ed known → compute the reduced moment resistance M_V,Rd.
      - Inverse  : M_V,Rd known → back-calculate the corresponding V_Ed.

    Returns
    -------
    float or None
        M_V,Rd  in forward mode.
        V_Ed    in inverse mode (printed, not returned).
    """
    print("=== Interaction M-V ===")

    V_Ed = float(input("V_Ed (enter 0 to back-calculate V_Ed from a known M_V,Rd): "))
    fy   = float(input("fy: "))
    t_w  = float(input("t_w: "))

    # --- V_pl,Rd -----------------------------------------------------------
    known_V = bool(int(input("V_pl,Rd already known? (1 = yes / 0 = no): ")))
    if known_V:
        V_pl_rd = float(input("V_pl,Rd: "))
        choice  = None                      # section type unknown yet
    else:
        V_pl_rd, choice = V_pl_Rd(t_w=t_w, fy=fy)   # choice: 1 = I y-y, 2 = H y-y

    # --- Section type (if not already determined by V_pl_Rd) ---------------
    def ask_section_type():
        print("Section type:")
        print("  0 – General")
        print("  1 – I  (bending about strong axis y-y)")
        print("  2 – H  (bending about strong axis y-y)")
        return int(input("Choice: "))

    # =======================================================================
    # CASE 1 : V_Ed > V_pl,Rd / 2  →  shear reduces the moment resistance
    # =======================================================================
    if V_Ed > V_pl_rd / 2:
        print("V_Ed > V_pl,Rd / 2  →  shear limits the moment resistance.")
        rho = (2 * V_Ed / V_pl_rd - 1) ** 2

        if choice is None:
            choice = ask_section_type()

        # --- General cross-section -----------------------------------------
        if choice not in (1, 2):
            print("General section")
            fyr = (1 - rho) * fy
            print(f"  Reduced yield strength fyr = {fyr:.2f}")

            plastic = bool(int(input("Plastic (1) or Elastic (0) section? ")))
            if plastic:
                W_pl     = float(input("W_pl: "))
                M_V_Rd   = fyr * W_pl / gamma_M[0]
                print(f"M_V,pl,Rd = {M_V_Rd:.2f}")
                return M_V_Rd
            else:
                W_el     = float(input("W_el: "))
                M_V_Rd   = fyr * W_el / gamma_M[0]
                print(f"M_V,el,Rd = {M_V_Rd:.2f}")
                return M_V_Rd

        # --- I / H cross-section (bending y-y) ------------------------------
        else:
            print("I / H section")
            A_w  = A_w_I_H(t_w=t_w)
            W_pl = float(input("W_y,pl: "))
            M_V_Rd = (W_pl - rho * A_w ** 2 / (4 * t_w)) * fy / gamma_M[0]
            print(f"M_V,y,Rd = {M_V_Rd:.2f}")
            return M_V_Rd

    # =======================================================================
    # CASE 2 : V_Ed = 0 (tbd)  →  back-calculate V_Ed from a known M_V,Rd
    # =======================================================================
    elif V_Ed == 0:
        print("Inverse mode: determining V_Ed from a known M_V,Rd.")

        if choice is None:
            choice = ask_section_type()

        M_V_rd = float(input("M_V,Rd (target): "))

        # --- General cross-section -----------------------------------------
        if choice not in (1, 2):
            print("General section")
            plastic = bool(int(input("Plastic (1) or Elastic (0) section? ")))
            if plastic:
                W    = float(input("W_pl: "))
            else:
                W    = float(input("W_el: "))
            # From M_V,Rd = (1-rho)*fy*W/γ_M0  and  rho = (2*V_Ed/V_pl,rd - 1)²
            #   → V_Ed = (sqrt(1 - M_V,rd*γ_M0/(fy*W)) + 1) * V_pl,rd / 2
            V_Ed = (( 1 - M_V_rd * gamma_M[0] / (fy * W) ) ** 0.5 + 1) * V_pl_rd / 2

        # --- I / H cross-section (bending y-y) ------------------------------
        else:
            print("I / H section")
            A_w  = A_w_I_H(t_w=t_w)
            W_pl = float(input("W_y,pl: "))
            # From M_V,y,Rd = (W_pl - rho*A_w²/(4*t_w))*fy/γ_M0
            #   → rho = (W_pl - M_V,rd*γ_M0/fy) * 4*t_w / A_w²
            #   → V_Ed = (sqrt(rho) + 1) * V_pl,rd / 2
            rho  = (W_pl - M_V_rd * gamma_M[0] / fy) * 4 * t_w / A_w ** 2
            V_Ed = (rho ** 0.5 + 1) * V_pl_rd / 2

        print(f"V_Ed = {V_Ed:.2f}")
        return V_Ed

    # =======================================================================
    # CASE 3 : V_Ed ≤ V_pl,Rd / 2  →  no M-V interaction
    # =======================================================================
    else:
        print("V_Ed ≤ V_pl,Rd / 2  →  No M-V interaction.")
        plastic = bool(int(input("Plastic (1) or Elastic (0) section? ")))
        if plastic:
            M_rd = M_pl_Rd(fy=fy)
            print(f"M_pl,Rd = {M_rd:.2f}")
        else:
            M_rd = M_el_Rd(fy=fy)
            print(f"M_el,Rd = {M_rd:.2f}")
        return M_rd