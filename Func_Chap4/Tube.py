from constant import epsilon2

def classify_tube():
    d  = float(input("d : "))
    t  = float(input("t : "))
    fy = float(input("fy: "))

    if d <= 0 or t <= 0 or fy not in epsilon2:
        print("d, t > 0")
        print("fy:", list(epsilon2.keys()))
        return None

    r = d / t
    e = epsilon2[fy]

    if   r <= 50 * e: c = 1
    elif r <= 70 * e: c = 2
    elif r <= 90 * e: c = 3
    else:
        print("Class 4")
        print("cfr: EN 1993-1-6")
        return 4

    print("Class {}".format(c))
    return c
