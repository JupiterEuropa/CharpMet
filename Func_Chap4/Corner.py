from epsilon import epsilon
from .section_class_function import *
def classify_corner():
    number_of_cantilevered_compressed_wall = int(input("Comp wall: "))
    number_of_cantilevered_compressed_flexed_wall = int(input("Comp-flex: "))
    fy = float(input("fy: "))
    classification_results = []

    if number_of_cantilevered_compressed_wall + number_of_cantilevered_compressed_flexed_wall > 2:
        print("Too many walls. Max 2.")
    
    elif fy not in epsilon:
        print("fy:", list(epsilon.keys()))
    
    else:
        
        for i in range(number_of_cantilevered_compressed_wall):
            print("Wall", i+1)
            classification_results.append(cantilevered_compressed_wall(epsilon[fy]))
            
        for i in range(number_of_cantilevered_compressed_flexed_wall):
            print("Wall", i+1)
            classification_results.append(cantilevered_compressed_flexed_wall(epsilon[fy]))

        if max(classification_results) > 2:
            print("Special case")
            h = float(input("h :"))
            b = float(input("b :"))
            t = float(input("t :"))
            if h <= 0 or b <= 0 or t <= 0:
                print("h,b,t > 0")                
            
            if h/t <= 15*epsilon[fy] and (b+h)/2/t <= 11.5*epsilon[fy]:
                print("Class 3")
                
            else:
                print("Class 4")
                
        else:
            print("Class:", max(classification_results))
            