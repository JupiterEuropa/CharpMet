from Func_Chap5.V_pl_Rd     import V_pl_Rd
from Func_Chap5.Int_M_V     import Int_M_V
from Func_Chap5.Flexion     import M_Rd
from Func_Chap5.Traction    import N_pl_Rd
from Func_Chap5.Compression import N_c_Rd
from Func_Chap5.Int_M_M     import Int_M_M
from Func_Chap5.Int_M_N     import Int_M_N
from Func_Chap5.Int_M_M_N   import Int_M_M_N
from Func_Chap5.Int_M_M_N_V import Int_M_M_N_V

MENU = [
    (1, "Traction",    N_pl_Rd),
    (2, "Compression", N_c_Rd),
    (3, "Flexion",     M_Rd),
    (4, "Shear",       V_pl_Rd),
    (5, "Int M-V",     Int_M_V),
    (6, "Int M-M",     Int_M_M),
    (7, "Int M-N",     Int_M_N),
    (8, "Int M-M-N",   Int_M_M_N),
    (9, "Int M-M-N-V", Int_M_M_N_V),
]

print("Choose a function:")
while True:
    for k, label, _ in MENU:
        print("{}: {}".format(k, label))

    try:
        choice = int(input("Choice (1-9): "))
    except ValueError:
        print("Enter 1-9")
        continue

    fn = next((f for k, _, f in MENU if k == choice), None)
    if fn:
        fn()
        break
    else:
        print("Enter 1-9")