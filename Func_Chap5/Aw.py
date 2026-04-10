def A_w_I_H(A=None, A_w=None, b=None, t_f=None,
            h_w=None, t_w=None, welded_rolled=None):

    if A_w is None:
        A_w = float(input("A_w known(0/1): "))

    if A_w != 0:
        print("A_w = {:.4g}".format(A_w))
        return A_w

    if welded_rolled is None:
        print("0: Welded")
        print("1: Rolled")        
        welded_rolled = input("Choice: ") == "1"

    if welded_rolled:
        if A   is None: A   = float(input("A: "))
        if b   is None: b   = float(input("b: "))
        if t_f is None: t_f = float(input("t_f: "))
        A_w = A - 2*b*t_f
    else:
        if t_w is None: t_w = float(input("t_w: "))
        if h_w is None: h_w = float(input("h_w: "))
        A_w = t_w * h_w

    print("A_w = {:.4g}".format(A_w))
    return A_w
