MENU = [
    (1, "Tract"),
    (2, "Compr"),
    (3, "Flexion"),
    (4, "Shear"),
    (5, "M-V"),
    (6, "M-M"),
    (7, "M-N"),
    (8, "M-M-N"),
]

print("Choose a function:")
while True:
    for i in range(0, len(MENU), 2):
        k1, label1 = MENU[i]
        line = "{}: {}".format(k1, label1)
        if i + 1 < len(MENU):
            k2, label2 = MENU[i + 1]
            line += "  {}: {}".format(k2, label2)
        print(line)

    try:
        choice = int(input("Choice (1-8): "))
    except ValueError:
        print("Enter 1-8")
        continue

    if choice == 1:
        from Func_Chap5.Traction import N_pl_Rd
        N_pl_Rd()
    elif choice == 2:
        from Func_Chap5.Compression import N_c_Rd
        N_c_Rd()
    elif choice == 3:
        from Func_Chap5.Flexion import M_Rd
        M_Rd()
    elif choice == 4:
        from Func_Chap5.V_pl_Rd import V_pl_Rd
        V_pl_Rd()
    elif choice == 5:
        from Func_Chap5.Int_M_V import Int_M_V
        Int_M_V()
    elif choice == 6:
        from Func_Chap5.Int_M_M import Int_M_M
        Int_M_M()
    elif choice == 7:
        from Func_Chap5.Int_M_N import Int_M_N
        Int_M_N()
    elif choice == 8:
        from Func_Chap5.Int_M_M_N import Int_M_M_N
        Int_M_M_N()
    else:
        print("Enter 1-8")
        continue
    
    break