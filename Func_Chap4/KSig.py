def k_sigma():
    print("k_sigma")
    sigma1 = float(input("sigma1: "))
    sigma2 = float(input("sigma2: "))
    case   = int(input("Case (1/2/3): "))

    if case not in (1, 2, 3):
        print("Invalid case")
        return None
    if sigma1 <= 0:
        print("sigma1 > 0")
        return None

    psi = sigma2 / sigma1

    if case == 1:
        if   psi >= 1:  ks = 4.0
        elif psi >  0:  ks = 8.02 / (1 + psi)
        elif psi > -1:  ks = 7.81 - 6.29*psi + 9.78*psi**2
        else:           ks = 23.9

    elif case == 2:
        if   psi >= 1:  ks = 0.43
        elif psi > -1:  ks = 0.57 - 0.21*psi + 0.07*psi**2
        else:           ks = 0.85

    else:
        if   psi >= 1:  ks = 0.43
        elif psi >  0:  ks = 0.579 / (0.34 + psi)
        elif psi > -1:  ks = 1.7 - 5*psi + 17.1*psi**2
        else:           ks = 23.8

    print("k_sigma = {:.4g}".format(ks))
    return ks
