from epsilon import epsilon2
def classify_tube():
    d = float(input("d :"))
    t = float(input("t :"))
    fy= float(input("fy: "))

    if d <= 0 or t <= 0 or fy not in epsilon2:
        print("d,t > 0")
        print("fy:", list(epsilon2.keys()))
        return None

    d_over_t = d/t

    if d_over_t <= 50*epsilon2[235]:
        print("This section is of class 1")
    elif d_over_t <= 70*epsilon2[235]:
        print("This section is of class 2")
    elif d_over_t <= 90*epsilon2[235]:
        print("This section is of class 3")
    else:
        print("This section may be of class 4")
        print("cfr: EN 1993-1-6")