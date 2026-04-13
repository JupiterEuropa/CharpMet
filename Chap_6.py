MENU = [
    (0, "L_fl"),
    (1, "N_cr"),
    (2, "N_b,Rd"),
]

while True:
    for k, label in MENU:
        print("{}: {}".format(k, label))

    try:
        choice = int(input("Choice (0-2): "))
    except ValueError:
        print("Enter 0-2")
        continue

    if choice == 0:
        from Func_Chap6.L_fl import Lfl
        Lfl()
    elif choice == 1:
        from Func_Chap6.N_cr import Ncr
        Ncr()
    elif choice == 2:
        from Func_Chap6.M_buckling import N_b_Rd
        N_b_Rd()
    else:
        print("Enter 0-2")
        continue
    
    break