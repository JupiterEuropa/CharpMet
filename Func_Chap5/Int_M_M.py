from .Int_M_M_function import Int_M_M_cl1_cl2
from .Int_M_M_N_function import Int_M_M_N_cl3
def Int_M_M():
    print("Int M-M Calc")
    while True:
        
        choice_class = int(input("Class of section: "))      

        if choice_class in (1, 2):
            Int_M_M_cl1_cl2()
            break
        elif choice_class == 3:
            Int_M_M_N_cl3(Int_M_M= True)
            break
        else:
            print("Enter 1-3")
            input("Any key to continue...")
            continue
        