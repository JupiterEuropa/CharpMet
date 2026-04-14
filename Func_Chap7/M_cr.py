

def M_cr():
    from math import pi, sqrt
    from constant import E, nu
    

    G = E / (2*(1+nu))

    print("M_cr")
    C_1, C_2 = _C()
    z_g = float(input("z_g: "))
    I_z = float(input("I_z: "))
    h = float(input("h: "))
    t_f = float(input("t_f: "))
    L = float(input("L: "))*1000  # convert to mm
    k_w = float(input("k_w: "))
    k_z = float(input("k_z: "))
    I_w = _I_w(h=h, t_f=t_f, I_z=I_z)
    I_t = _I_t(h=h, t_f=t_f, b=None, t_w=None)

    C_2z_g = C_2 * z_g
    EI_z = E * I_z
    k_zL_2 = (k_z * L)**2
    root = sqrt((k_z/k_w)**2 * I_w/I_z + k_zL_2*G*I_t/pi**2/EI_z + C_2z_g**2)
    M_cr = C_1 * pi**2 * EI_z / k_zL_2 * (root - C_2z_g) * 1e-6 # convert to kNm
    print("M_cr: {:.4f}".format(M_cr))
    return M_cr

def _C():
    from constant import lerp_2d
    print("C_1/C_2:")
    print("1: Dual Moment")
    print("2: Load on beam")
    print("3: Tables C_1/C_2")
    choice_C1 = int(input("C_1 (1-): "))

    if choice_C1 == 1:
        while True:
            M_1 = float(input("M_1: "))
            M_2 = float(input("M_2: "))
            if M_1 == M_2 == 0:
                print("Both moments are 0.")
                continue
            else:
                break
        
        if abs(M_1) >= abs(M_2):
            psi = M_2 / M_1
        else:
            psi = M_1 / M_2

        C_1 = min(2.6, 1.77 - 1.04*psi + 0.27*psi**2)
        C_2 = 0
    
    elif choice_C1 == 2:
        C_1 = float(input("C_1 (0=a): "))
        C_2 = float(input("C_2: "))
        if C_1 == 0:
            alpha = float(input("alpha: "))
            C_1 = 1.28/alpha
    
    elif choice_C1 == 3:
        psi = {}
        u = {}
        C = {}
        psi_c = float (input("psi_c: "))
        u_c = float(input("u_c : "))

        for i in range(2):
            psi[i] = float(input("psi_{}: ".format(i+1)))
            u[i] = float(input("u_{}: ".format(i+1)))
        
        for k in range(2):
            C[k] = {}
            print("C_1-{}:".format(k+1))
            for i in range(2):
                C[k][i] = {}
                print("psi_{}: {:.4f}".format(i+1, psi[i]))
                for j in range(2):
                    print("u_{}: {:.4f}".format(j+1, u[j]))
                    C[k][i][j] = float(input("C_1-{}-{}: ".format(i+1, j+1)))


        C_1 = lerp_2d(psi_c, u_c, psi[0], psi[1], u[0], u[1], C[0][0][0], C[0][0][1], C[0][1][0], C[0][1][1])
        C_2 = lerp_2d(psi_c, u_c, psi[0], psi[1], u[0], u[1], C[1][0][0], C[1][0][1], C[1][1][0], C[1][1][1])

    print("C_1: {:.4f}".format(C_1))
    print("C_2: {:.4f}".format(C_2))
    return C_1, C_2
      
def _I_w(h : None, t_f : None, I_z : None):
    print("Calc I_w")
    if I_z is None:
        I_z = float(input("I_z: "))
    if h is None:
        h = float(input("h: "))
    if t_f is None:
        t_f = float(input("t_f: "))
    
    I_w = I_z * (h - t_f)**2 / 4
    print("I_w: {:.4f}".format(I_w))
    return I_w

def _I_t(h : None, t_f : None, b : None, t_w : None):
    print("Calc I_t")
    if h is None:
        h = float(input("h: "))
    if t_f is None:
        t_f = float(input("t_f: "))
    if b is None:
        b = float(input("b: "))
    if t_w is None:
        t_w = float(input("t_w: "))

    I_t = (2*b*t_f**3 + (h-2*t_f)*t_w**3) / 3
    print("I_t: {:.4f}".format(I_t))
    return I_t