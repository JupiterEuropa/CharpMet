from constant import epsilon

def classify_corner():
    from .section_class_function import (
        cantilevered_compressed_wall,
        cantilevered_compressed_flexed_wall,
    )
    n_comp      = int(input("Comp wall: "))
    n_comp_flex = int(input("Comp-flex: "))
    fy          = float(input("fy: "))

    if n_comp + n_comp_flex > 2:
        print("Max 2 walls")
        return None

    if fy not in epsilon:
        print("fy:", list(epsilon.keys()))
        return None

    e       = epsilon[fy]
    results = []

    for i in range(n_comp):
        print("Wall {}".format(i + 1))
        results.append(cantilevered_compressed_wall(e))

    for i in range(n_comp_flex):
        print("Wall {}".format(i + 1))
        results.append(cantilevered_compressed_flexed_wall(e))

    if max(results) <= 2:
        print("Class {}".format(max(results)))
        return max(results)

    print("Special case")
    h = float(input("h: "))
    b = float(input("b: "))
    t = float(input("t: "))

    if h <= 0 or b <= 0 or t <= 0:
        print("h, b, t > 0")
        return None

    if h/t <= 15*e and (b+h)/2/t <= 11.5*e:
        print("Class 3")
        return 3
    else:
        print("Class 4")
        return 4
