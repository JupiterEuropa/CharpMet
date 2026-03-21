from math import pi
from .L_fl import Lfl
from constant import E

def Ncr(L=None, K=None, L_fl=None, I=None, asm=None):
    print("N_cr Calc")
    if L_fl is None: L_fl = Lfl(L=L, K=K, asm=asm, I=I)
    if I    is None: I    = float(input("I: "))
    N_cr = pi**2 * E * I / L_fl**2
    print("N_cr = {:.4g}".format(N_cr))
    return N_cr
