from Func_Chap4.Classes import *
from Func_Chap4.Corner import *
from Func_Chap4.CritSig import *
from Func_Chap4.KSig import *
from Func_Chap4.Tube import *
from Func_Chap4.section_class_function import *


print("Choose a function:")
print("1. Critical Sigma")
print("2. K Sigma")
print("3. Classify Section")
print("4. Classify Corner")
print("5. Classify Tube")
choice = int(input("Your choice: "))

if choice == 1:
    critical_sigma()
elif choice == 2:
    k_sigma()
elif choice == 3:
    classify_section()
elif choice == 4:
    classify_corner()
elif choice == 5:
    classify_tube()
else:
    print("Invalid choice. Please enter a number between 1 and 5.")
    exit()