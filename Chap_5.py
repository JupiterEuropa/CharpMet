from Func_Chap5.V_pl_Rd import *
from Func_Chap5.Int_M_V import *

print("Choose:")
print("4: Shear")
print("5: Interaction M-V")


choice = int(input("Choice: "))
while True:
    if choice == 4:
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
