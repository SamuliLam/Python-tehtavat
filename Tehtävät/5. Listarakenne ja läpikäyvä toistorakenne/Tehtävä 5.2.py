lista = []

while True:
    userInput = input("Anna numero: ")
    if userInput == "":
        break

    lista.append(float(userInput))

lista.sort(reverse=True)

print("Viisi suurinta numeroa ovat: \n")

for i in range(5):
    print(lista[i])