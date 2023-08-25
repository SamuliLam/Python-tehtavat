import random
arpakuutiolkm = int(input("Anna arpakuutioiden lukumäärä: "))

i = 0
sum = 0
a = []

while i < arpakuutiolkm:
    randomNumber = random.randint(1,6)
    a.append(randomNumber)
    i += 1

for x in a:
    print(x)
    sum += x

print("Arpakuutioiden summa on : "+str(sum))