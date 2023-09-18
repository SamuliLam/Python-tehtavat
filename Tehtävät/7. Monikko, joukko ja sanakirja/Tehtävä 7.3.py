lentoasemat = {}

choice = input(
    "1. Syötä uusi lentoasema \n"
    "2. Hae lentoaseman tiedot \n"
    "3. Lopeta ohjelma \n"
    "Kirjoita haluamaasi syötettä vastaava numero: \n"
)

while choice != "3":

    if choice == "1":
        lentoasema_nimi = input("Anna lentoaseman nimi: ")
        icao_koodi = input("Anna lentoaseman ICAO-koodi: ")
        lentoasemat[icao_koodi] = lentoasema_nimi

    elif choice == "2":
        search_icao = input("Anna sen lentoaseman ICAO-koodi, jonka tiedot haluat: \n")
        if search_icao in lentoasemat:
            print("Lentoaseman nimi: " + lentoasemat[search_icao])

    choice = input(
        "1. Syötä uusi lentoasema \n"
        "2. Hae lentoaseman tiedot \n"
        "3. Lopeta ohjelma \n"
        "Kirjoita haluamaasi syötettä vastaava numero: \n"
    )



