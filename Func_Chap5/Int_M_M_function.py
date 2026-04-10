from .Flexion_function import M_pl_Rd
from constant import gamma_M

def Int_M_M_cl1_cl2(fy=None, W_y_pl=None, W_z_pl=None,
                    M_y_Ed=None, M_z_Ed=None, choice_section=None):
    print("Int M-M cl1/cl2")

    while True:
        if M_y_Ed is None or M_y_Ed == 0:
            M_y_Ed = abs(float(input("M_y_Ed (0=tbd): ")))
        if M_z_Ed is None or M_z_Ed == 0:
            M_z_Ed = abs(float(input("M_z_Ed (0=tbd): ")))
        if M_y_Ed == 0 and M_z_Ed == 0:
            print("Both moments = 0")
        else:
            break

    if fy is None:
        fy = float(input("fy: "))

    if choice_section is None:
        print("Section type:")
        print("1: I/H")
        print("2: Tube")
        print("3: Rect")
        choice_section = int(input("Choice: "))

    print("Strong axis")
    M_pl_y_rd = M_pl_Rd(fy=fy, W_pl=W_y_pl)
    print("Weak axis")
    M_pl_z_rd = M_pl_Rd(fy=fy, W_pl=W_z_pl)

    if choice_section == 1:
        alpha, beta = 2, 1
    elif choice_section == 2:
        alpha, beta = 2, 2
    else:
        alpha, beta = 1.66, 1.66

    if M_y_Ed == 0:
        M_y_Ed = (1 - (M_z_Ed / M_pl_z_rd)**beta)**(1/alpha) * M_pl_y_rd
        print("M_y,Ed = {:.4g}".format(M_y_Ed))
        return M_y_Ed
    else:
        M_z_Ed = (1 - (M_y_Ed / M_pl_y_rd)**alpha)**(1/beta) * M_pl_z_rd
        print("M_z,Ed = {:.4g}".format(M_z_Ed))
        return M_z_Ed

def Int_M_M_cl3():
    print("Int M-M cl3")    

    while True:
        
        M_y_Ed = float(input("M_y_Ed: (0=tbd)"))
        M_z_Ed = float(input("M_z_Ed: (0=tbd)"))

        if M_y_Ed == 0 and M_z_Ed == 0:
            print("Both moments = 0")
        else:
            break

    
    W_el_y = float(input("W_el_y: "))
    W_el_z = float(input("W_el_z: "))
    fy     = float(input("fy: "))

    if M_y_Ed == 0:
        M_z_Ed = (fy/gamma_M[0]*1e-6 - (M_y_Ed / W_el_y )) * W_el_z
        print("M_z,Ed = {:.4g}".format(M_z_Ed))
        return M_z_Ed
    else:
        M_y_Ed = (fy/gamma_M[0]*1e-6 - (M_z_Ed / W_el_z )) * W_el_y
        print("M_y,Ed = {:.4g}".format(M_y_Ed))
        return M_y_Ed
    
