import math

pizza = []

diameter1 = float(input("Anna ensimmäisen pizzan halkaisija senttimetreinä: "))
price1 = float(input("Anna ensimmäisen pizzan hinta euroina: "))

diameter2 = float(input("Anna ensimmäisen pizzan halkaisija senttimetreinä: "))
price2 = float(input("Anna ensimmäisen pizzan hinta euroina: "))


def pizza_cost_calculator(diameter, price):
    radius = diameter / 2
    pizza_area = math.pi * radius ** 2
    pizza_price = pizza_area / price
    return pizza_price


pizza.append(pizza_cost_calculator(diameter1, price1))
pizza.append(pizza_cost_calculator(diameter2, price2))

if pizza[0] < pizza[1]:
    print("Toinen pizza on edullisempi!")
else:
    print("Ensimmäinen pizza on edullisempi!")
