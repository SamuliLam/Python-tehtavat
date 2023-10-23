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

class Talo:
    def __init__(self, alinkerros_nro, ylinkerros_nro, hissi_lkm):
        self.alinkerros_nro = alinkerros_nro
        self.ylinkerros_nro = ylinkerros_nro
        self.hissi_lkm = hissi_lkm
        self.hissit = []

    def aja_hissiä(self, hissin_nro, kohdekerros):
        self.hissit[hissin_nro-1].siirry_kerrokseen(kohdekerros)

#Pääohjelma

talo = Talo(1, 10, 3)

for i in range(talo.hissi_lkm):
    talo.hissit.append(Hissi(talo.alinkerros_nro, talo.ylinkerros_nro))

talo.aja_hissiä(1, 5)
talo.aja_hissiä(2, 7)
talo.aja_hissiä(3, 9)

for i in range(talo.hissi_lkm):
    print(f'Hissi {i+1} on kerroksessa {talo.hissit[i].nykyinen_kerros}')