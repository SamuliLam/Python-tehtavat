class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettumatka = 0


a1 = Auto("ABC-123", 142)

print(f"Auton rekisteritunnus on {a1.rekisteritunnus}, huippunopeus {a1.huippunopeus} km/h, nopeus {a1.nopeus} km/h, kuljettu matka {a1.kuljettumatka}")