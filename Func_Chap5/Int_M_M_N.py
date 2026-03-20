from .Int_M_M_N_function import *

def Int_M_M_N():
    print("Int M-M-N Calc")
    choice_class = int(input("Class of section: "))

    if choice_class in (1, 2):
        Int_M_M_N_cl1_cl2()
    else:
        Int_M_M_N_cl3()