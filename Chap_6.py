MENU = [
    (0, "L_fl"),
    (1, "N_cr"),
    (2, "N_b,Rd"),
]

from Menu_Display import printMenu
choice = printMenu(MENU)

if choice == 0:
    from Func_Chap6.L_fl import Lfl
    Lfl()
elif choice == 1:
    from Func_Chap6.N_cr import Ncr
    Ncr()
elif choice == 2:
    from Func_Chap6.N_b_Rd import N_b_Rd
    N_b_Rd()