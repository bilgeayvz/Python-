class canli:
    def __init__(self, yas=None, isim=None, cins=None, kilo=None):
        self.yas = yas
        self.isim = isim
        self.cins = cins
        self.kilo = kilo

    def bosaltim(self):
        print("boşaltım yapıldı")

    def solunum(self):
        print("solunum yapıldı")

    def beslenme(self):
        print("beslenme yapıldı")

    def buyume(self):
        print("büyüme gerçekleşti")


class insan(canli):
    meslek = ""

    def dusun(self):
        print("Düşünüyorum öyleyse varım")

    def tanit(self):
        print("Adım {}, mesleğim {}".format(self.isim, self.meslek))


class hayvan(canli):
    evcilmi = True
    omurgalimi = True
    habitatineresi = ""
    ayaksayisi = 0

    def ozellik(self):
        print("Evcil mi:{}\n Omurgalı mı: {}\n Habitatı neresi: {}\n Ayak sayısı: {}".format(self.evcilmi,
                                                                                             self.omurgalimi,
                                                                                             self.habitatineresi,
                                                                                             self.ayaksayisi))
        print("Yaşı: {}\n Adı: {}\n Cinsi: {}\n".format(self.yas, self.isim, self.cins))


class bitki(canli):
    ciceklimi = True
    bitkiortusu = ""

    def fotosentez(self):
        print("Fotosentez oldu")


kaucuk = bitki()
kaucuk.ciceklimi = False
kaucuk.bitkiortusu = "Maki"
print("Çiçekli mi:{}\n Bitki örtüsü:{}\n".format(kaucuk.ciceklimi, kaucuk.bitkiortusu))
kaucuk.fotosentez()

a = hayvan()
a.isim = "Kaplumbağa"
a.ozellik()

kopek = hayvan(2, "Max", "Golden", 5)
kopek.evcilmi = True
kopek.omurgalimi = True
kopek.habitatineresi = "Kara"
kopek.ayaksayisi = 4
kopek.ozellik()

kedi = hayvan(3, "Boncuk", "Tekir", 4)
kedi.habitatineresi = "Kara"
kedi.ayaksayisi = 4
kedi.ozellik()

kus = hayvan(2, "Maviş", "Muhabbet kuşu", 0.5)
kus.habitatineresi = "Kara"
kus.ayaksayisi = 2
kus.ozellik()

