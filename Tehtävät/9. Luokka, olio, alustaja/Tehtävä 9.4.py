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


autot = []

for i in range(10):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)

kilpailuJatkuu = True
while kilpailuJatkuu:

    for auto in autot:
        auto.kiihdytä(random.randint(-15, 15))
        auto.kulje(1)
        if auto.kuljettumatka > 10000:
            kilpailuJatkuu = False

for auto in autot:
    print(f"Rekisteritunnus: {auto.rekisteritunnus}, Kuljettumatka: {auto.kuljettumatka}")
