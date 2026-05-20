MENU = [
    (1, "Bolts preload"),
    (2, "Corner bolted single web"),
    (3, "Corner welded single web"),
    (4, "T U single web"),
    (5, "Fix Shear and Traction"),
    (6, "Block shear"),
    (7, "Welds")

]

from Menu_Display import printMenu

choice = printMenu(MENU)

if choice == 1:
    from Func_Chap8.F_P_Cd import F_p_Cd
    F_p_Cd()
elif choice == 2:
    from Func_Chap8.N_U_Rd_bolts import N_u_Rd_bolted
    N_u_Rd_bolted()
elif choice == 3:
    from Func_Chap8.Corner_Single_web_welded import Corner_single_web_welded
    Corner_single_web_welded()
elif choice == 4:
    from Func_Chap8.T_U_Single_Web import T_U_single_web
    T_U_single_web()
elif choice == 5:
    from Func_Chap8.F_Rd_Fix_V_T import F_Rd_Fix_V_T
    F_Rd_Fix_V_T()
elif choice == 6:
    from Func_Chap8.Block_Shear import Block_shear
    Block_shear()
elif choice == 7:
    from Func_Chap8.Welds import Welds
    Welds()
