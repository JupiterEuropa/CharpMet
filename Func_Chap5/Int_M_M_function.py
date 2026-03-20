
from Flexion import M_pl_Rd
def Int_M_M_cl1_cl2(A = None, A_w = None, b = None, t_f = None, t_w = None, 
                    h = None, h_w = None, r = None, number_of_webs = None, 
                    fy = None, N_Ed = None, M_y_Ed = None, M_z_Ed = None, 
                    W_y_pl = None, W_z_pl = None, choice_section = None
                    ):
    print("Int M-M cl1/cl2 Calc")
    while M_y_Ed is None or M_z_Ed is None or flag:
        
        if M_y_Ed is None or M_y_Ed == 0:
            M_y_Ed = abs(float(input("M_y_Ed: (tbd: 0)")))
        if M_z_Ed is None or M_z_Ed == 0:
            M_z_Ed = abs(float(input("M_z_Ed: (tbd: 0)")))

        flag = (M_y_Ed == 0 and M_z_Ed == 0)
        if flag:
            print("Both moment are 0")
            input("Any key to continue...")
            continue

    if fy is None:
        fy = float(input("fy: "))
    if choice_section is None:
        print("Choose:")
        print("1: I/H ")
        print("2: Tube")
        print("3: Rect")
        
        choice_section = int(input("Choice: "))

    
    print("Strong axis")
    M_pl_y_rd = M_pl_Rd(fy= fy, W_pl= W_y_pl)

    print("Weak axis")
    M_pl_z_rd = M_pl_Rd(fy= fy, W_pl= W_z_pl)

    
    
    if choice_section == 1:
        alpha = 2
        beta = 1
    elif choice_section ==2:
        alpha = 2
        beta = 2
    else:
        alpha = 1.66
        beta = 1.66

    if M_y_Ed == 0:
        M_y_Ed = (1 - (M_z_Ed/M_pl_z_rd)**beta)**(1/alpha) * M_pl_y_rd
    else:
        M_z_Ed = (1 - (M_y_Ed/M_pl_y_rd)**alpha)**(1/beta) * M_pl_z_rd