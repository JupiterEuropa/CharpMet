from epsilon import epsilon
from .section_class_function import *

def classify_section():
    print("Cantilevered walls")
    number_of_cantilevered_compressed_wall = int(input("Comp. wall: "))
    number_of_cantilevered_compressed_flexed_wall = int(input("Comp-flex wall: "))
    print("Internal walls")
    number_of_internal_compressed_wall = int(input("Comp. wall: "))
    number_of_internal_flexed_wall = int(input("Flex wall: "))
    number_of_internal_compressed_flexed_wall = int(input("Comp-flex wall: "))

    fy = float(input("fy: "))
    if fy not in epsilon:
        print("fy must be one of\nthe following:", list(epsilon.keys()))
    else:

        classification_results = []

        for i in range(number_of_cantilevered_compressed_wall):
            print("Cant. comp wall:", i+1)
            classification_results.append(cantilevered_compressed_wall(epsilon[fy]))
        for i in range(number_of_cantilevered_compressed_flexed_wall):
            print("Cant. comp-flex:", i+1)
            classification_results.append(cantilevered_compressed_flexed_wall(epsilon[fy]))
        for i in range(number_of_internal_compressed_wall):
            print("Int. comp wall:", i+1)
            classification_results.append(internal_compressed_wall(epsilon[fy]))
        for i in range(number_of_internal_flexed_wall):
            print("Int. flex wall:", i+1)
            classification_results.append(internal_flexed_wall(epsilon[fy]))
        for i in range(number_of_internal_compressed_flexed_wall):
            print("Int. comp-flex:", i+1)
            classification_results.append(internal_compressed_flexed_wall(epsilon[fy]))

        print("Section class:", max(classification_results))