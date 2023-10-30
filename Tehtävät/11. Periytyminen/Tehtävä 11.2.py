import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettumatka = 0

    def kiihdytä(self, nopeudenmuutos):
        if (self.nopeus + nopeudenmuutos > self.huippunopeus):
            self.nopeus = self.huippunopeus
        elif self.nopeus + nopeudenmuutos < 0:
            self.nopeus = 0
        else:
            self.nopeus = self.nopeus + nopeudenmuutos

    def kulje(self, tuntimäärä):
        self.kuljettumatka += self.nopeus * tuntimäärä

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)


class Polttomoottiauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        self.bensatankin_koko = bensatankin_koko
        super().__init__(rekisteritunnus, huippunopeus)


sähköauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottiauto("ACD-123",165,32.3)

sähköauto.nopeus = 55
polttomoottoriauto.nopeus = 75
sähköauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f'Kuljtettu matka: {sähköauto.kuljettumatka} kilometriä')
print(f'Kuljettu matka: {polttomoottoriauto.kuljettumatka} kilometriä')

