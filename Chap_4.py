from Func_Chap4.Classes   import classify_section
from Func_Chap4.Corner    import classify_corner
from Func_Chap4.CritSig   import critical_sigma
from Func_Chap4.KSig      import k_sigma
from Func_Chap4.Tube      import classify_tube

MENU = [
    (1, "Critical Sigma",   critical_sigma),
    (2, "K Sigma",          k_sigma),
    (3, "Classify Section", classify_section),
    (4, "Classify Corner",  classify_corner),
    (5, "Classify Tube",    classify_tube),
]

print("Choose a function:")
while True:
    for k, label, _ in MENU:
        print("{}: {}".format(k, label))

    try:
        choice = int(input("Choice (1-5): "))
    except ValueError:
        print("Enter 1-5")
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
        print("Enter 1-5")