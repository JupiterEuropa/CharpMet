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
    (1, "Tract",    N_pl_Rd),
    (2, "Compr",    N_c_Rd),
    (3, "Flexion",  M_Rd),
    (4, "Shear",    V_pl_Rd),
    (5, "M-V",      Int_M_V),
    (6, "M-M",      Int_M_M),
    (7, "M-N",      Int_M_N),
    (8, "M-M-N",    Int_M_M_N),
    (9, "M-M-N-V",  Int_M_M_N_V),
]

print("Choose a function:")
while True:
    for i in range(0, len(MENU), 2):
        k1, label1, _ = MENU[i]
        line = "{}: {}".format(k1, label1)
        if i + 1 < len(MENU):
            k2, label2, _ = MENU[i + 1]
            line += "  {}: {}".format(k2, label2)
        print(line)

    try:
        choice = int(input("Choice (1-9): "))
    except ValueError:
        print("Enter 1-9")
        continue

    fn = None
    for k, _, f in MENU:
        if k == choice:
            fn = f
            break
    
    if fn:
        fn()
        break
    else:
        print("Enter 1-9")