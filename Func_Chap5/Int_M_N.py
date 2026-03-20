from Int_M_N_function import *
from Int_M_M_N_function import Int_M_M_N_cl3

def Int_M_N(A = None, A_w = None, fy = None, b = None, t_f = None, N_Ed = None, choice_section = None, 
            choice_class = None, choice_flex = None, t_w = None, h_w = None, h = None, welded_rolled = None):
    
    print("Int M-N Calc")
    if choice_class == None:
        choice_class = int(input("Class of section: "))

    if choice_section == None:
        print("Choose:")
        print("1: I/H ")
        print("2: Rect/Tube")
        choice_class = int(input("Class of section: "))

    if choice_flex == None:
        print("Choose:")
        print("1: Strong axis ")
        print("2: Weak axis")
        choice_flex = int(input("Choice: "))

    
    if choice_class in (1, 2) and choice_section == 1 and choice_flex == 1: #cl1/cl2, I/H, strong axis
        Moment = Int_M_N_I_y_y_cl1_cl2(A = A, A_w = A_w, b = b, t_f = t_f, t_w = t_w, h_w = h_w, welded_rolled = welded_rolled,  
                    fy = fy, N_Ed = N_Ed)
        
    elif choice_class in (1, 2) and choice_section == 1 and choice_flex == 2: #cl1/cl2, I/H, weak axis
        Moment = Int_M_N_I_z_z_cl1_cl2(A = A, A_w = A_w, b = b, t_f = t_f, t_w = t_w, 
                    h_w = h_w, welded_rolled= welded_rolled,
                    fy = fy, N_Ed = N_Ed)
        
    elif choice_class in (1, 2) and choice_section == 2 and choice_flex == 1: #cl1/cl2, Rect/Tube, strong axis
        Moment = Int_M_N_Rect_Tube_y_y_cl1_cl2(A = A, A_w = A_w, b = b, t_f = t_f, fy = fy, N_Ed = N_Ed)

    elif choice_class in (1, 2) and choice_section == 2 and choice_flex == 2: #cl1/cl2, Rect/Tube, weak axis
        Moment = Int_M_N_Rect_Tube_z_z_cl1_cl2(A = A, A_w = A_w, b = b, t_w = t_w, h = h, fy = fy, N_Ed = N_Ed)
        
    elif choice_class == 3:
        Moment = Int_M_M_N_cl3(Int_M_M=0, Int_M_N=1)
    
    return Moment