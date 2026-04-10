from Func_Chap5.V_pl_Rd     import V_pl_Rd
from Func_Chap5.Int_M_V     import Int_M_V
from Func_Chap5.Flexion     import M_Rd
from Func_Chap5.Traction    import N_pl_Rd
from Func_Chap5.Compression import N_c_Rd
from Func_Chap5.Int_M_M     import Int_M_M
from Func_Chap5.Int_M_N     import Int_M_N
from Func_Chap5.Int_M_M_N   import Int_M_M_N

MENU = [
    (1, "Tract",    "Func_Chap5.Traction", "N_pl_Rd"),
    (2, "Compr",    "Func_Chap5.Compression", "N_c_Rd"),
    (3, "Flexion",  "Func_Chap5.Flexion", "M_Rd"),
    (4, "Shear",    "Func_Chap5.V_pl_Rd", "V_pl_Rd"),
    (5, "M-V",      "Func_Chap5.Int_M_V", "Int_M_V"),
    (6, "M-M",      "Func_Chap5.Int_M_M", "Int_M_M"),
    (7, "M-N",      "Func_Chap5.Int_M_N", "Int_M_N"),
    (8, "M-M-N",    "Func_Chap5.Int_M_M_N", "Int_M_M_N"),
]

print("Choose a function:")
while True:
    for i in range(0, len(MENU), 2):
        k1, label1, module_path, func_name = MENU[i]
        line = "{}: {}".format(k1, label1)
        if i + 1 < len(MENU):
            k2, label2, module_path, func_name = MENU[i + 1]
            line += "  {}: {}".format(k2, label2)
        print(line)

    try:
        choice = int(input("Choice (1-8): "))
    except ValueError:
        print("Enter 1-8")
        continue

    fn = None
    for k, label, module_path, func_name in MENU:
        if k == choice:
            module = __import__(module_path, fromlist=[func_name])
            fn = getattr(module, func_name)
            fn()
            break
    
    if fn:
        break
    else:
        print("Enter 1-8")