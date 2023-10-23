class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettumatka = 0

    def kiihdytä(self, nopeudenmuutos):
        if (self.nopeus + nopeudenmuutos > self.huippunopeus):
            self.nopeus = 142
        elif self.nopeus + nopeudenmuutos < 0:
            self.nopeus = 0
        else:
            self.nopeus = self.nopeus + nopeudenmuutos



a1 = Auto("ABC-123", 142)

a1.kiihdytä(30)
a1.kiihdytä(70)
a1.kiihdytä(50)

print(f"Auton nopeus: {a1.nopeus} km/h")
a1.kiihdytä(-200)
print(f"Auton nopeus: {a1.nopeus} km/h")
