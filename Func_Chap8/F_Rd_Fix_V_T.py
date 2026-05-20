MENU = [
    (1, "Bolts Shear"),
    (2, "Rivets Shear"),
    (3, "Diametral Pressure"),
    (4, "Bolts Traction"),
    (5, "Rivets Traction"),
    (6, "Bolts Punching"),
    (7, "Bolts Shear Traction")
]

def  F_Rd_Fix_V_T():
    from Menu_Display import printMenu
    choice = printMenu(MENU)
    if choice == 1:
        F_v_Rd_Bolts()
    elif choice == 2:
        F_v_Rd_Rivets()
    elif choice == 3:
        F_b_Rd()
    elif choice == 4:
        F_t_Rd_Bolts()
    elif choice == 5:
        F_t_Rd_Rivets()
    elif choice == 6:
        B_p_Rd()
    elif choice == 7:
        F_vt_Rd_Bolts()
    return

def F_v_Rd_Bolts(f_ub=None):
    from constant import gamma_M
    alpha_v = float(input("alpha_v: "))
    if f_ub is None:
        f_ub = float(input("f_ub: "))
    A = float(input("A: "))

    F_v_rd = alpha_v * A * f_ub / gamma_M[2] * 1e-3 # kN
    print("F_v,Rd = {:.4f}".format(F_v_rd))
    return F_v_rd

def F_v_Rd_Rivets():
    from constant import gamma_M
    if f_ur is None:
        f_ur = float(input("f_ur: "))
    A0 = float(input("A0: "))

    F_v_rd = 0.6 * f_ur * A0 / gamma_M[2] * 1e-3 # kN
    print("F_v,Rd = {:.4f}".format(F_v_rd))
    return F_v_rd

def F_b_Rd():
    from constant import gamma_M
    f_ub = float(input("f_ub: "))
    fu = float(input("fu: "))
    e1 = float(input("e1: "))
    e2 = float(input("e2: "))
    p1 = float(input("p1: "))
    p2 = float(input("p2: "))
    d0 = float(input("d0: "))
    d = float(input("d: "))
    t = float(input("t: "))
    choice = int(input("Bolts: Internal(0) or End(1): "))
    if choice == 0:
        alpha_b = min(p1/3/d0 - 0.25, f_ub/fu, 1)
        k1 = min(1.4 * p2/d0-1.7, 2.5)
    elif choice == 1:
        alpha_b = min(e1/3/d0 , f_ub/fu, 1)
        k1 = min(2.8 * e2/d0-1.7, 2.5)

    
    F_b_Rd = k1*alpha_b * fu * d *t / gamma_M[2] * 1e-3 # kN
    print("F_b,Rd = {:.4f}".format(F_b_Rd))
    return F_b_Rd

def F_t_Rd_Bolts(f_ub=None):
    from constant import gamma_M
    if f_ub is None:
        f_ub = float(input("f_ub: "))
    As = float(input("As: "))
    k2 = float(input("k2: "))

    F_t_Rd = k2*f_ub * As/gamma_M[2] * 1e-3 # kN
    print("F_t,Rd = {:.4f}".format(F_t_Rd))
    return F_t_Rd

def F_t_Rd_Rivets():
    from constant import gamma_M
    f_ur = float(input("f_ur: "))
    A0 = float(input("A0: "))

    F_t_rd = 0.6 * f_ur * A0 / gamma_M[2] * 1e-3 # kN
    print("F_t,Rd = {:.4f}".format(F_t_rd))
    return F_t_rd


def B_p_Rd():
    from constant import gamma_M
    from math import pi
    fu = float(input("fu: "))
    dm = float(input("dm: "))
    tp = float(input("tp: ")) 
    B_p_Rd = 0.6 * pi * dm * tp * fu / gamma_M[2] * 1e-3 # kN
    print("B_p,Rd = {:.4f}".format(B_p_Rd))
    return B_p_Rd

def F_vt_Rd_Bolts():
    from constant import gamma_M

    while True:
        F_v_Ed = float(input("F_v,Ed: (0=tbd)"))
        F_t_Ed = float(input("F_t,Ed: (0=tbd)"))
        if F_v_Ed == 0 and F_t_Ed == 0:
            print("Both forces = 0")
        else:
            break

    f_ub = float(input("f_ub: "))
    F_v_rd = F_v_Rd_Bolts(f_ub=f_ub) # kN
    F_t_rd = F_t_Rd_Bolts(f_ub=f_ub) # kN
    
    if F_v_Ed == 0:
        F_v_Ed = (1 - (F_t_Ed / 1.4 / F_t_rd))*F_v_rd
        print("F_v,Ed = {:.4f}".format(F_v_Ed))
        return F_v_Ed
    elif F_t_Ed == 0:
        F_t_Ed = (1 - (F_v_Ed / F_v_rd))*F_t_rd*1.4
        print("F_t,Ed = {:.4f}".format(F_t_Ed))
        return F_t_Ed
    else:
        if F_v_Ed / F_v_rd + F_t_Ed / 1.4 / F_t_rd <= 1:
            print("The bolt resists")
        else:
            print("The bolt fails")
        return None