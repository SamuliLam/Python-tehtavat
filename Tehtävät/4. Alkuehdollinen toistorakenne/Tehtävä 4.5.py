unInput = input("Anna käyttäjätunnus: ")
pwInput = input("Anna salasana: ")


i = 0
username = "python"
password = "rules"

while unInput != username or pwInput != password:
    print("Väärät kirjautumisteidot, anna tiedot uudelleen")
    i += 1
    if i == 5:
        print("Pääsy evätty")
        break

    unInput = input("Anna käyttäjätunnus: ")
    pwInput = input("Anna salasana: ")


    if unInput == username and pwInput == password:
        print("Tervetuloa")
        break