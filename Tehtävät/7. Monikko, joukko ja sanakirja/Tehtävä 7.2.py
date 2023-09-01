nimet = set()

while True:
    nimi = input("Anna nimi (tyhjä rivi lopettaa): ")

    if nimi == "":
        break

    if nimi not in nimet:
        nimet.add(nimi)
        print("Uusi nimi")
    else:
        print("Aiemmin syötetty nimi")

for n in nimet:
    print(n)
