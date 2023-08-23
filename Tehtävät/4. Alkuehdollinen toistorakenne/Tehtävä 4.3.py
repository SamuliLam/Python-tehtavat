userinput = input("Anna luku: ")
suurin = None
pienin = None

while userinput != "":
    userinput = input("Anna luku: ")
    try:
        if suurin is None or int(userinput) > int(suurin):
            suurin = userinput

        if pienin is None or int(userinput) < int(pienin):
            pienin = userinput
    except:
        print("invalid output")

print("Numeroista pienin on: "+str(pienin)+" Numeroista suurin on: "+str(suurin))