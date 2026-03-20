from Traction import N_pl_Rd
from Int_M_N import Int_M_N
from Aw import A_w_I_H
def Int_M_M_N_cl1_cl2():
    print("Int M-M-N cl1/cl2 Calc")

    while flag:   

        M_y_Ed = abs(float(input("M_y_Ed: (tbd: 0)")))    
        M_z_Ed = abs(float(input("M_z_Ed: (tbd: 0)")))    
        N_Ed = abs(float(input("N_Ed: ")))

        flag = (M_y_Ed == 0 and M_z_Ed ==0) or N_Ed == 0
        if flag:
            print("Moments or N_Ed = 0")
            input("Any key to continue...")
            continue

    A = float(input("A: "))
    fy = float(input("fy: "))


    N_pl_rd = N_pl_Rd(A= A, fy= fy)

    while True:
        print("Choose:")
        print("1: I/H ")
        print("2: Tube")
        print("3: Rect")
        
        choice_section = int(input("Choice: "))
        if choice_section in (1,2,3):
            break
        else:
            print("Choice invalid")
            input("Any key to continue...")
            continue

    if choice_section == 1:
        print("Section I/H")        
        welded_rolled = bool(input("Section Welded/Rolled (1/0)"))
        h_w = float(input("h_w: "))
        
    else:
        print("Section Rect/Tube")
        h = float(input("h: "))
    
    t_w = float(input("t_w: "))
    b = float(input("b: "))
    t_f =float(input("t_f: "))    
    
    
    if choice_section == 1:
        A_w = A_w_I_H(A= A, b= b, t_f= t_f, t_w= t_w, h_w= h_w, welded_rolled= welded_rolled)
        
    
    M_N_y_rd = Int_M_N(A = A, A_w = A_w, fy = fy, b = b, t_f = t_f, N_Ed = N_Ed, choice_section = choice_section, 
            choice_class = 1, choice_flex = 1, t_w = t_w, h_w = h_w, h = h, welded_rolled = welded_rolled)
    M_N_z_rd = Int_M_N(A = A, A_w = A_w, fy = fy, b = b, t_f = t_f, N_Ed = N_Ed, choice_section = choice_section, 
            choice_class = 1, choice_flex = 2, t_w = t_w, h_w = h_w, h = h, welded_rolled = welded_rolled)
    
    n = N_Ed/N_pl_rd

    if choice_section == 1:
        alpha = 2
        beta = max(1, 5*n)
    elif choice_section == 2:
        alpha = 2
        beta = 2
    elif choice_section == 3:
        alpha = min(6, 1.66/(1-1.13*n**2))
        beta = alpha
    

    if M_y_Ed == 0:
        print("Determining M_y_Ed")
        M_y_Ed = (1 - (M_z_Ed/M_N_z_rd)**beta)**(1/alpha) * M_N_y_rd
        print("M_y,Ed= ", M_y_Ed)
    elif M_z_Ed == 0:
        print("Determining M_z_Ed")
        M_z_Ed = (1 - (M_y_Ed/M_N_y_rd)**alpha)**(1/beta) * M_N_z_rd
        print("M_z,Ed= ", M_z_Ed)
        
def Int_M_M_N_cl3(Int_M_M: bool = 0, Int_M_N: bool = 0): #Setting Int_M_M to True for Interraction M-M for class 3, same for Int_M_N
    if Int_M_M:
        print("Int M-M cl3 Calc")
    elif Int_M_N:
        print("Int M-N cl3 Calc")
    else:
        print("Int M-M-N cl3 Calc")

    while True:
        if  Int_M_M:
            N_Ed =0           
        else:
            N_Ed = float(input("N_Ed: "))

        if Int_M_N:
            M_y_Ed = float(input("M_Ed: "))
        else:
            M_y_Ed = float(input("M_y_Ed: "))
            M_z_Ed = float(input("M_z_Ed: "))
        
        if (Int_M_M and M_y_Ed == 0 and M_z_Ed == 0):
            print("Both moment are 0")
            input("Any key to continue...")
            continue 
        elif (not Int_M_M and not Int_M_N and [N_Ed , M_y_Ed, M_z_Ed].count(0.0) >= 2):
            print("2 vars are 0")
            input("Any key to continue...")
            continue
        elif (Int_M_N and N_Ed == 0 and M_y_Ed == 0):
            print("M_Ed and N_Ed are 0")
            input("Any key to continue...")
            continue
        else:
            break

    if not Int_M_M:
        A = float(input("A: "))
    else:
        A = 1

    if Int_M_N:
        W_el_y = float(input("W_el: "))
        W_el_z = 1
    else:            
        W_el_z = float(input("W_el_z: "))
        W_el_y = float(input("W_el_y: "))

    fy = float(input("fy: "))

    if N_Ed == 0 and not Int_M_M:
        N_Ed =( fy - M_z_Ed/W_el_z - M_y_Ed/W_el_y) * A
        print("N_Ed: ", N_Ed)
    elif M_y_Ed == 0:
        M_y_Ed = (fy - N_Ed/A - M_z_Ed/W_el_z) * W_el_y
        print("M_y_Ed: ", M_y_Ed)
    elif M_z_Ed == 0 and not Int_M_N:
        M_z_Ed = (fy - N_Ed/A - M_y_Ed/W_el_y) * W_el_z