MENU = [
    (1, "Complete verification of welds"),
    (2, "Simplified verification of welds"),
]


def Welds():
    from Menu_Display import printMenu
    choice = printMenu(MENU)
    if choice == 1:
        complete_verification()
    elif choice == 2:
        simplified_verification()

    return

def complete_verification():
    from constant import gamma_M, beta_w
    from math import sqrt
    print("Complete verification of welds")
    fu = float(input("fu: "))
    fy = float(input("fy: "))
    sigma_p = float(input("sigma T: "))
    tau_p = float(input("tau T: "))
    tau_v = float(input("tau //: "))
    sqrt_part = sqrt(sigma_p**2 + 3*(tau_p**2 + tau_v**2))
    fu_reduced = fu/gamma_M[2]/beta_w[fy]
    fu_sigma = 0.9*fu/gamma_M[2]
    print("Combined stress = {:.4f} MPa".format(sqrt_part))
    print("Reduced strength = {:.4f} MPa".format(fu_reduced))
    print("Sigma limit = {:.4f} MPa".format(fu_sigma))
    if sqrt_part <= fu_reduced and sigma_p <= fu_sigma:
        print("Welds will hold")
    else:
        print("Welds will fail")
    
    return

    

def simplified_verification():
    from constant import gamma_M, beta_w
    from math import sqrt
    print("Simplified verification of welds")
    a = float(input("a: "))
    fu = float(input("fu: "))
    fy = float(input("fy: "))
    F_w_rd = a * fu/gamma_M[2]/sqrt(3)/beta_w[fy]
    print("F_w,Rd = {:.4g} N/mm".format(F_w_rd))

    return F_w_rd