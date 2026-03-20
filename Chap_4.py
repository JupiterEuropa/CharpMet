from Func_Chap4.Classes import *
from Func_Chap4.Corner import *
from Func_Chap4.CritSig import *
from Func_Chap4.KSig import *
from Func_Chap4.Tube import *
from Func_Chap4.section_class_function import *

print("Choose a function:")
while True:
    
    print("1. Critical Sigma")
    print("2. K Sigma")
    print("3. Classify Section")
    print("4. Classify Corner")
    print("5. Classify Tube")
    choice = int(input("Your choice: "))

    if choice == 1:
        critical_sigma()
        break
    elif choice == 2:
        k_sigma()
        break
    elif choice == 3:
        classify_section()
        break
    elif choice == 4:
        classify_corner()
        break
    elif choice == 5:
        classify_tube()
        break
    else:
        print("Invalid")
        print("Enter 1-5")
        input("Any key to continue...")
        continue