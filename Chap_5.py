from Func_Chap5.V_pl_Rd import *
from Func_Chap5.Int_M_V import *
from Func_Chap5.Flexion import *
from Func_Chap5.Traction import *
from Func_Chap5.Compression import *
from Func_Chap5.Int_M_M import *
from Func_Chap5.Int_M_N import *
from Func_Chap5.Int_M_M_N import *
from Func_Chap5.Int_M_N_V import *

print("Choose a function:")
while True:
    
    print("1: Traction")
    print("2: Compression")
    print("3: Flexion")
    print("4: Shear")
    print("5: Interaction M-V")
    print("6: Interaction M-M")
    print("7: Interaction M-N")
    print("8: Interaction M-M-N")
    print("9: Interaction M-N-V")
    choice = int(input("Choice: "))

    if choice == 1:
        N_pl_Rd()
    elif choice == 2:
        N_c_Rd()
    elif choice == 3:
        M_Rd
    elif choice == 4:
        V_pl_Rd()
        break
    elif choice == 5:
        Int_M_V()
        break
    elif choice ==6:
        Int_M_M()
    elif choice ==7:
        Int_M_N()
    elif choice ==8:
        Int_M_M_N()
    elif choice ==9:
        Int_M_N_V()
    else:
        print("Invalid")
        print("Enter 1-9")
        input("Any key to continue...")
        continue
