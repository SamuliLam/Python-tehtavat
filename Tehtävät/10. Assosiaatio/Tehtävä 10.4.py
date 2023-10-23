import random


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
        self.kuljettumatka += self.nopeus * tuntimäärä

class Kilpailu:
    def __init__(self, nimi, pituus_km, autolista):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autolista = autolista

    def tunti_kuluu(self):
        for auto in self.autolista:
            auto.kiihdytä(random.randint(-15, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        for auto in self.autolista:
            print(f'Auto {auto.rekisteritunnus} on kulkenut {auto.kuljettumatka}')

#auto ei saa kulkea yli 8000km
    def kilpailu_ohi(self):
        for auto in self.autolista:
            if auto.kuljettumatka >= self.pituus_km:
                return False
        return True

#Pääohjelma


autot = []

for i in range(10):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)

#Tehdään kilpailuolio nimeltä Suuri romiralli
kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

#Kilpailu käyntiin
while kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()

kilpailu.tulosta_tilanne()