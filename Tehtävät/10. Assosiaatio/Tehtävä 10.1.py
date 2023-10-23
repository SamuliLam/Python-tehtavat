class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = 1

    def siirry_kerrokseen(self, kerros):
        if kerros < self.alin_kerros or kerros > self.ylin_kerros:
            print("Kerrosta ei ole olemassa")
        else:
            self.nykyinen_kerros = kerros

    def kerros_ylös(self):
        if self.nykyinen_kerros == self.ylin_kerros:
            print("Hissi on jo ylimmässä kerroksessa")
        else:
            self.nykyinen_kerros += 1

    def kerros_alas(self):
        if self.nykyinen_kerros == self.alin_kerros:
            print("Hissi on jo alimmassa kerroksessa")
        else:
            self.nykyinen_kerros -= 1

hissi = Hissi(1, 10)

hissi.siirry_kerrokseen(9)
print(hissi.nykyinen_kerros)
hissi.kerros_alas()
hissi.siirry_kerrokseen(11)
print(hissi.nykyinen_kerros)
hissi.siirry_kerrokseen(1)
print(hissi.nykyinen_kerros)