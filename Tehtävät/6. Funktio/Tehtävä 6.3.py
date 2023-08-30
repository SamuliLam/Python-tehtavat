import math

gallons = input("Anna bensiinin määrä nestegallonoina: ")

def gallon_to_liter_converter(gallonamount):
    liters = float(gallonamount * 3.785)
    return liters

while gallons != "":
    gallon_to_liter_converter(gallons)