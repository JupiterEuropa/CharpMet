def k_sigma():
    sigma1 = float(input("sigma1: "))
    sigma2 = float(input("sigma2: "))
    case = int(input("Case: "))
    if case not in [1, 2, 3]:
        print("Invalid case number. ")
        print("Please enter 1, 2, or 3.")
        return None
    if sigma1 <= 0:
        print("sigma1 must be greater than 0.")
        return None
    psi = sigma2/sigma1
    if case == 1:
        if psi >= 1:
            k_sigma = 4
        elif psi == 0:
            k_sigma = 7.81
        elif psi <= -1:
            k_sigma = 23.9
        elif psi >0 and psi < 1:
            k_sigma = 8.02/(1+psi)
        elif psi > -1 and psi < 0:
            k_sigma = 7.81 - 6.29*psi + 9.78*psi**2
    elif case == 2:
        if psi >= 1:
            k_sigma = 0.43
        elif psi == 0:
            k_sigma = 0.57
        elif psi <= -1:
            k_sigma = 0.85
        else:
            k_sigma = 0.57-0.21*psi+0.07*psi**2
    elif case == 3:
        if psi >= 1:
            k_sigma = 0.43
        elif psi == 0:
            k_sigma = 1.70
        elif psi <= -1:
            k_sigma = 23.8
        elif psi >0 and psi < 1:
            k_sigma = 0.579/(0.34+psi)
        elif psi > -1 and psi < 0:
            k_sigma = 1.7 - 5*psi + 17.1*psi**2
        

    print("k_sigma = ", k_sigma)
    return k_sigma

k_sigma()