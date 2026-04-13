def Int_M_M_N():
    print("Int M-M-N Calc")
    try:
        choice_class = int(input("Section class: "))
    except ValueError:
        print("Enter 1-3")
        return None

    if choice_class in (1, 2):
        from .Int_M_M_N_function import Int_M_M_N_cl1_cl2
        Int_M_M_N_cl1_cl2()
    else:
        from .Int_M_M_N_function import Int_M_M_N_cl3
        Int_M_M_N_cl3()
