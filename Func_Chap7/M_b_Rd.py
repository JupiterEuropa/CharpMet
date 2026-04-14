def M_b_Rd():
    from math import sqrt
    from constant import gamma_M
    from Func_Chap7.M_cr import M_cr
    from Func_Chap5.Flexion import M_Rd
    from Func_Chap6.N_b_Rd import alpha

    print("M_b,Rd Calc")

    if input("M_cr known (1/0): ") == "1":
        M_cr_value = float(input("M_cr: "))
    else:
        M_cr_value = M_cr()
    
    W_y = float(input("W_y: "))
    fy = float(input("fy: "))
    M_y = M_Rd(W_y=W_y, fy=fy)

    lambda_red = sqrt(M_y / M_cr_value)

    if lambda_red <= 0.2:
        print("Lambda_red <=0.2")
        print("M_b,Rd = M_cr = M_y")
        M_b_Rd = M_y
    else:
        alpha_value = alpha()
        phi = 0.5 * (1 + alpha_value * (lambda_red - 0.2) + lambda_red**2)
        xi = min(1.0, 1/(phi + sqrt(phi**2 - lambda_red**2)))
        M_b_Rd = xi * W_y * fy / gamma_M[0] * 1e-6 # convert to kNm


    print("M_b,Rd: {:.4f}".format(M_b_Rd))
    return M_b_Rd