from .Int_M_M_function import Int_M_M_cl1_cl2, Int_M_M_cl3

def Int_M_M():
    print("Int M-M Calc")
    while True:
        try:
            choice_class = int(input("Section class: "))
        except ValueError:
            print("Enter 1-3")
            continue

        if choice_class in (1, 2):
            Int_M_M_cl1_cl2()
            break
        elif choice_class == 3:
            Int_M_M_cl3()
            break
        else:
            print("Enter 1-3")
