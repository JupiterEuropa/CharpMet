from epsilon import epsilon
from .section_class_function import *
def classify_corner():
    number_of_cantilevered_compressed_wall = int(input("paroi comp: "))
    number_of_cantilevered_compressed_flexed_wall = int(input("paroi comp flex: "))
    fy = float(input("fy: "))
    classification_results = []

    if number_of_cantilevered_compressed_wall + number_of_cantilevered_compressed_flexed_wall > 2:
        print("Trop de parois a classer")
    
    elif fy not in epsilon:
        print("fy must be one of the following values: ", list(epsilon.keys()))
    
    else:
        
        for i in range(number_of_cantilevered_compressed_wall):
            print("Paroi en console comp ", i+1)
            classification_results.append(cantilevered_compressed_wall(epsilon[fy]))
            
        for i in range(number_of_cantilevered_compressed_flexed_wall):
            print("Paroi en console comp flex ", i+1)
            classification_results.append(cantilevered_compressed_flexed_wall(epsilon[fy]))

        if max(classification_results) > 2:
            print("Cas particulier")
            h = float(input("h :"))
            b = float(input("b :"))
            t = float(input("t :"))
            if h <= 0 or b <= 0 or t <= 0:
                print("h, b and t must be greater than 0.")                
            
            if h/t <= 15*epsilon[fy] and (b+h)/2/t <= 11.5*epsilon[fy]:
                print("This section is of class 3")
                
            else:
                print("This section is of class 4")
                
        else:
            print("Classe de la section: ", max(classification_results))
            