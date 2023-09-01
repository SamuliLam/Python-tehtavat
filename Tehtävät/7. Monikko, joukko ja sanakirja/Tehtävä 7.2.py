nimi = input("Anna nimi: ")

nimet = {}

while nimi != "":
    if nimi not in nimet:
        nimet.add(nimi)
        print("Uusi nimi")
    else:
        print("Aiemmin syötetty nimi")


for n in nimet:
    print(n)
