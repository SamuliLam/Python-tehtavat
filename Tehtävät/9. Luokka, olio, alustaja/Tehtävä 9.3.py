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

    def kulje(self, tuntimäärä):
        self.kuljettumatka = self.nopeus * tuntimäärä


a1 = Auto("ABC-123", 142)

a1.kiihdytä(60)
a1.kulje(1.5)

print(f"Auton kulkema matka: {a1.kuljettumatka} km")
