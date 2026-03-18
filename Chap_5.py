from Func_Chap5.V_pl_Rd import *
from Func_Chap5.Int_M_V import *
from Func_Chap5.Flexion import *
from Func_Chap5.Traction import *
from Func_Chap5.Compression import *

print("Choose:")
print("1: Traction")
print("2: Compression")
print("3: Flexion")
print("4: Shear")
print("5: Interaction M-V")


choice = int(input("Choice: "))
while True:
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
    else:
        print("Invalid")
        print("Enter 4")
        input("Any key to continue...")
        continue
