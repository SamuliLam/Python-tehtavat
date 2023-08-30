import random

tahkot = int(input("Anna nopan maksimisilmäluku: "))


def random_number(maxnumber):
    rnumber = random.randint(1, maxnumber)
    return rnumber


generated_number = random_number(tahkot)

while generated_number != tahkot:
    print("Numero " + str(generated_number) + " oli väärin.")
    generated_number = random_number(tahkot)

print("Nopan maksimisilmäluku: " + str(generated_number))
