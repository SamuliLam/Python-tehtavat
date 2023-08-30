import random


def random_number():
    rnumber = random.randint(1, 6)
    return rnumber


generated_number = random_number()

while generated_number != 6:
    print("Numero " + str(generated_number) + " oli väärin.")
    generated_number = random_number()

print("Löysit oikean numeron: " + str(generated_number))
