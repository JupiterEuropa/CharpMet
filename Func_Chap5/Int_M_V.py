def Int_M_V(): # M -V interaction only applies for plastic interaction, so no need to ask for elastic/plastic
    print("M-V Interaction")
    while True:
        V_Ed = float(input("V_Ed (0=tbd): "))
        M_V_rd = float(input("M_V,Rd (0=tbd): "))
        if V_Ed == 0 and M_V_rd == 0:
            print("V_Ed, M_V,Rd both 0")
        else:
            break
    fy   = float(input("fy: "))
    t_w  = float(input("t_w: "))

    from .V_pl_Rd import V_pl_Rd
    from constant import gamma_M
    from Func_Chap5.Flexion_function import M_pl_Rd, M_el_Rd
    from .Aw import A_w_I_H

    known_V = input("V_pl,Rd known(1/0):") == "1"
    if known_V:
        V_pl_rd = float(input("V_pl,Rd: "))
        choice  = None
    else:
        V_pl_rd, choice, A_w = V_pl_Rd(t_w=t_w, fy=fy)

    if V_Ed > V_pl_rd / 2:
        print("V > V_pl/2: M reduced")
        rho = (2 * V_Ed / V_pl_rd - 1) ** 2

        if choice is None:
            choice = _ask_section_type()

        if choice not in (1, 2):
            fyr  = (1 - rho) * fy
            print("fyr = {:.4g}".format(fyr))
            W    = float(input("W_pl: " ))
            M_V_Rd = fyr * W / gamma_M[0]*1e-6
            print("M_V,Rd = {:.4g}".format(M_V_Rd))
            return M_V_Rd

        else:
            A_w    = A_w_I_H(t_w=t_w)
            W_pl   = float(input("W_y,pl: "))
            M_V_Rd = (W_pl - rho * A_w**2 / (4*t_w)) * fy / gamma_M[0]*1e-6
            print("M_V,Rd = {:.4g}".format(M_V_Rd))
            return M_V_Rd

    elif V_Ed == 0:
        print("Inverse mode")

        if choice is None:
            choice = _ask_section_type()


        if choice not in (1, 2):
            W       = float(input("W_pl: "))
            V_Ed = ((1 - M_V_rd * gamma_M[0] / (fy * W))**0.5 + 1) * V_pl_rd / 2

        else:
            A_w  = A_w_I_H(t_w=t_w)
            W_pl = float(input("W_y,pl: "))
            rho  = (W_pl - M_V_rd * gamma_M[0] / fy) * 4*t_w / A_w**2
            V_Ed = (rho**0.5 + 1) * V_pl_rd / 2 * 1e-3

        print("V_Ed = {:.4g}".format(V_Ed))
        return V_Ed

    else:
        print("V <= V_pl/2: no int.")
        M_rd = M_pl_Rd(fy=fy)
        return M_rd
