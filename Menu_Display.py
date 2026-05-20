def printMenu(MENU) -> int:
    print("Choose a function:")
    while True:
        for k, label in MENU:
            print("{}: {}".format(k, label))

        try:
            choice = int(input("Choice ({}-{}): ".format(MENU[0][0], MENU[-1][0])))
        except ValueError:
            print("Enter {}-{}".format(MENU[0][0], MENU[-1][0]))
            continue
        if choice not in [k for k, _ in MENU]:
            print("Enter {}-{}".format(MENU[0][0], MENU[-1][0]))
            continue
        
        return choice
