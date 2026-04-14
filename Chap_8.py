MENU = [

]

while True:
    for k, label in MENU:
        print("{}: {}".format(k, label))

    try:
        choice = int(input("Choice (1-): "))
    except ValueError:
        print("Enter 1-")
        continue

    if choice == 1:
        pass