# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun
# ja ilmoittaa, onko se alkuluku. Tässä tehtävässä alkulukuja ovat luvut,
# jotka ovat jaollisia vain ykkösellä ja itsellään.


userInput = int(input("Anna kokonaisluku: "))

if userInput > 1:
    for i in range(2, (int(userInput/2)+1)):
        if (userInput % i) == 0:
            print("\n" + str(userInput) + " ei ole alkuluku")
            break
    else:
        print("\n" + str(userInput) + " on alkuluku")
else:
    print("\n" + str(userInput) + " ei ole alkuluku")