from constant import epsilon
from .section_class_function import (
    cantilevered_compressed_wall,
    cantilevered_compressed_flexed_wall,
    internal_compressed_wall,
    internal_flexed_wall,
    internal_compressed_flexed_wall,
)

def classify_section():
    print("Cantilevered walls")
    n_cant_comp      = int(input("Comp wall: "))
    n_cant_comp_flex = int(input("Comp-flex: "))
    print("Internal walls")
    n_int_comp       = int(input("Comp wall: "))
    n_int_flex       = int(input("Flex wall: "))
    n_int_comp_flex  = int(input("Comp-flex: "))
    fy               = float(input("fy: "))

    if fy not in epsilon:
        print("fy:", list(epsilon.keys()))
        return None

    e       = epsilon[fy]
    results = []

    walls = [
        (n_cant_comp,      "Cant comp",      cantilevered_compressed_wall),
        (n_cant_comp_flex, "Cant comp-flex", cantilevered_compressed_flexed_wall),
        (n_int_comp,       "Int comp",       internal_compressed_wall),
        (n_int_flex,       "Int flex",       internal_flexed_wall),
        (n_int_comp_flex,  "Int comp-flex",  internal_compressed_flexed_wall),
    ]

    for n, label, fn in walls:
        for i in range(n):
            print("{} {}".format(label, i + 1))
            results.append(fn(e))

    c = max(results)
    print("Section class {}".format(c))
    return c
