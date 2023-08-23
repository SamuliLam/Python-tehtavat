import random
cnumber = random.randint(1, 10)
print(str(cnumber))
guess = int(input("Yritä arvata oikea numero 1-10 väliltä: "))


while cnumber != guess:
    if cnumber < guess:
        print("Liian suuri arvaus")

    if cnumber > guess:
        print("Liian pieni arvaus")

    guess = int(input("Yritä arvata oikea numero 1-10 väliltä: "))

print("Oikein")