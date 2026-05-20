MENU = [
    (1, "M_cr"),
    (2, "M_b,Rd"),
]

from Menu_Display import printMenu
choice = printMenu(MENU)

if choice == 1:
    from Func_Chap7.M_cr import M_cr
    M_cr()
elif choice == 2:
    from Func_Chap7.M_b_Rd import M_b_Rd
    M_b_Rd()