import math

gallons = input("Anna bensiinin määrä nestegallonoina: ")


def gallon_to_liter_converter(gallonamount):
    return print(gallonamount * 3.785)


while gallons != "":
    gallon_to_liter_converter(float(gallons))
    gallons = input("Anna bensiinin määrä nestegallonoina: ")
