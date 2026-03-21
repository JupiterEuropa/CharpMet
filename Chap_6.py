from Func_Chap6.N_cr       import Ncr
from Func_Chap6.L_fl       import Lfl
from Func_Chap6.M_buckling import N_b_Rd

MENU = {
    0: ("L_fl",   Lfl),
    1: ("N_cr",   Ncr),
    2: ("N_b,Rd", N_b_Rd),
}

while True:
    for k, (label, _) in MENU.items():
        print("{}: {}".format(k, label))

    try:
        choice = int(input("Choice (0-2): "))
    except ValueError:
        print("Enter 0-2")
        continue

    if choice in MENU:
        MENU[choice][1]()
        break
    else:
        print("Enter 0-2")
