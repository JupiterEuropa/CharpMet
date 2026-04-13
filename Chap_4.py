MENU = [
    (1, "Critical Sigma"),
    (2, "K Sigma"),
    (3, "Classify Section"),
    (4, "Classify Corner"),
    (5, "Classify Tube"),
]

print("Choose a function:")
while True:
    for k, label in MENU:
        print("{}: {}".format(k, label))

    try:
        choice = int(input("Choice (1-5): "))
    except ValueError:
        print("Enter 1-5")
        continue

    if choice == 1:
        from Func_Chap4.CritSig import critical_sigma
        critical_sigma()
    elif choice == 2:
        from Func_Chap4.KSig import k_sigma
        k_sigma()
    elif choice == 3:
        from Func_Chap4.Classes import classify_section
        classify_section()
    elif choice == 4:
        from Func_Chap4.Corner import classify_corner
        classify_corner()
    elif choice == 5:
        from Func_Chap4.Tube import classify_tube
        classify_tube()
    else:
        print("Enter 1-5")
        continue
    
    break