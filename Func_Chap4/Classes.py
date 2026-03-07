from epsilon import epsilon
from section_class_function import *

def classify_section():
    print("Parois en console")
    number_of_cantilevered_compressed_wall = int(input("paroi comp: "))
    number_of_cantilevered_compressed_flexed_wall = int(input("paroi comp flex: "))
    print("Parois internes")
    number_of_internal_compressed_wall = int(input("paroi comp: "))
    number_of_internal_flexed_wall = int(input("paroi flex: "))
    number_of_internal_compressed_flexed_wall = int(input("paroi comp flex: "))

    fy = float(input("fy: "))
    if fy not in epsilon:
        print("fy must be one of the following values: ", list(epsilon.keys()))
        exit()

    classification_results = []

    for i in range(number_of_cantilevered_compressed_wall):
        print("Paroi console comp ", i+1)
        classification_results.append(cantilevered_compressed_wall(epsilon[fy]))
    for i in range(number_of_cantilevered_compressed_flexed_wall):
        print("Paroi console comp flex ", i+1)
        classification_results.append(cantilevered_compressed_flexed_wall(epsilon[fy]))
    for i in range(number_of_internal_compressed_wall):
        print("Paroi interne comp ", i+1)
        classification_results.append(internal_compressed_wall(epsilon[fy]))
    for i in range(number_of_internal_flexed_wall):
        print("Paroi interne flex ", i+1)
        classification_results.append(internal_flexed_wall(epsilon[fy]))
    for i in range(number_of_internal_compressed_flexed_wall):
        print("Paroi interne comp flex ", i+1)
        classification_results.append(internal_compressed_flexed_wall(epsilon[fy]))

    print("Classe de la section: ", max(classification_results))
    exit()