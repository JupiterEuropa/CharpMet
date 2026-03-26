from math import sqrt
# from .N_cr import Ncr

_BEAM_CHOICES = {
    1: ("Embed",       4),
    2: ("Articulated", 3),
    3: ("Same rot",    6),
    4: ("Opp rot",     2),
}

def _N_coeff(choice, N, N_cr):
    if choice == 1: return 1 - 0.4 * N / N_cr
    if choice == 2: return 1 - N / N_cr
    return           1 - 0.2 * N / N_cr

def _beam_K(tag):
    I = float(input("I_{}: ".format(tag)))
    if I == 0:
        return 0.0
    L = float(input("L_{}: ".format(tag)))

    for k, (label, _) in _BEAM_CHOICES.items():
        print("{}: {}".format(k, label))
    while True:
        try:
            choice = int(input("Choice: "))
            if choice in _BEAM_CHOICES:
                break
        except ValueError:
            pass
        print("Enter 1-4")

    coeff = _BEAM_CHOICES[choice][1]

    # if input("N in beam (1/0): ") == "1":
    #     # N     = float(input("N: "))
    #     # N_cr  = Ncr()
    #     # coeff_N = _N_coeff(choice, N, N_cr)
    # else:
    coeff_N = 1.0

    return coeff * I / L * coeff_N


def _K_asm(I_c=None, L_c=None, mobile_node=None):
    print("K Assembly Calc")
    if I_c is None: I_c = float(input("I_c: "))
    if L_c is None: L_c = float(input("L_c: "))

    K_c = 4 * I_c / L_c

    I_1 = float(input("I_1 (0=none): "))
    K_1 = 4 * I_1 / float(input("L_1: ")) if I_1 != 0 else 0.0

    I_2 = float(input("I_2 (0=none): "))
    K_2 = 4 * I_2 / float(input("L_2: ")) if I_2 != 0 else 0.0

    n_top = int(input("Top beams: "))
    K_1x  = sum(_beam_K("1_{}".format(i+1)) for i in range(n_top))

    n_bot = int(input("Bot beams: "))
    K_2x  = sum(_beam_K("2_{}".format(i+1)) for i in range(n_bot))

    n_sup = (K_c + K_1) / (K_c + K_1 + K_1x) if (K_c + K_1 + K_1x) else 0
    n_inf = (K_c + K_2) / (K_c + K_2 + K_2x) if (K_c + K_2 + K_2x) else 0
    print("n_sup = {:.4g}".format(n_sup))
    print("n_inf = {:.4g}".format(n_inf))

    if mobile_node is None:
        mobile_node = input("Mobile node (1/0): ") == "1"

    if mobile_node:
        K = sqrt(
            (1 - 0.2*(n_sup + n_inf) - 0.12*n_sup*n_inf) /
            (1 - 0.8*(n_sup + n_inf) + 0.6*n_sup*n_inf)
        )
    else:
        K = (
            (1 + 0.145*(n_sup + n_inf) - 0.265*n_sup*n_inf) /
            (2 - 0.364*(n_sup + n_inf) - 0.247*n_sup*n_inf)
        )

    print("K = {:.4g}".format(K))
    return K


def _K(asm=None, I_c=None, L_c=None):
    if asm is None:
        asm = input("Beam in assembly (1/0): ") == "1"
    if asm:
        return _K_asm(I_c=I_c, L_c=L_c)
    return float(input("K: "))


def Lfl(L=None, K=None, asm=None, I=None):
    print("L_fl Calc")
    if L is None: L = float(input("L: "))
    if K is None: K = _K(asm=asm, I_c=I, L_c=L)
    L_fl = K * L
    print("L_fl = {:.4g}".format(L_fl))
    return L_fl
