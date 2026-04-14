MENU = [
    (1, "M_cr"),
    (2, "M_b,Rd"),
]

while True:
    for k, label in MENU:
        print("{}: {}".format(k, label))

    try:
        choice = int(input("Choice (1-2): "))
    except ValueError:
        print("Enter 1-2")
        continue

    if choice == 1:
        from Func_Chap7.M_cr import M_cr
        M_cr()
    elif choice == 2:
        from Func_Chap7.M_b_Rd import M_b_Rd
        M_b_Rd()
    else:
        print("Enter 1-2")
        continue
    
    break