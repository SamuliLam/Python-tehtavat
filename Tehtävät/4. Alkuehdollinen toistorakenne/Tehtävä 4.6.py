import random
import math

pisteet = int(input("Anna arvottavien pisteiden lukumäärä: "))
pisteet1 = pisteet

isInside = float(0)

while pisteet1 > 0:

    x = random.random()
    y = random.random()

    if x**2+y**2<1:
        isInside += 1

    pisteet1 -= 1

print("Pi:n likiarvo on: "+ str(4*isInside / pisteet))

