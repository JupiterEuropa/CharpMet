def cantilevered_compressed_wall(fy: float):
    from math import sqrt
    c = float(input("c :"))
    t = float(input("t :"))

    if c <= 0 or t <= 0:
        print("c and t must be greater than 0.")
        return None
    
    epsilon = sqrt(235/fy)
    c_over_t = c/t

    if c_over_t <= 9*epsilon:
        print("This section is of class 1")
        return 1
    elif c_over_t <= 10*epsilon:
        print("This section is of class 2")
        return 2
    elif c_over_t <= 14*epsilon:
        print("This section is of class 3")
        return 3
    else:
        print("This section is of class 4")
        return 4

def cantilevered_compressed_flexed_wall (fy: float):
    from math import sqrt
    from k_sigma import k_sigma

    c = float(input("c :"))
    t = float(input("t :"))
    alpha = float(input("alpha :"))
    extremity_stress = bool(input("ext compressed(1/0):"))

    if c <= 0 or t <= 0:
        print("c and t must be greater than 0.")
        return None
    
    epsilon = sqrt(235/fy)
    c_over_t = c/t

    if extremity_stress and c_over_t <= 9*epsilon/alpha:
        print("This section is of class 1")
        return 1
    elif extremity_stress and c_over_t <= 10*epsilon/alpha:
        print("This section is of class 2")
        return 2
    elif not extremity_stress and c_over_t <= 9*epsilon/alpha/sqrt(alpha):
        print("This section is of class 1")
        return 1
    elif not extremity_stress and c_over_t <= 10*epsilon/alpha/sqrt(alpha):
        print("This section is of class 2")
        return 2
    else:
        k_sigma_value = k_sigma()
        if c_over_t <= 21*epsilon*sqrt(k_sigma_value):
            print("This section is of class 3")
            return 3
        else:
            print("This section is of class 4")
            return 4
