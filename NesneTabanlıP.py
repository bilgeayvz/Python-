'''
#ÖRNEK1
class Araba:
    marka=""
    renk=""
    plaka=""
    tekerlek_sayısı=4
araba1= Araba()
araba1.marka="Toyota"
araba1.renk="Beyaz"
araba1.plaka="14 A 148"
araba1.tekerlek_sayısı=3


araba2= Araba()
araba2.marka="BMW"
araba2.renk="Siyah"
araba2.plaka="08 HG 48"
araba2.tekerlek_sayısı=2

ebrununarabası= Araba()
ebrununarabası.marka="Ford"
ebrununarabası.renk="Kırmızı"
ebrununarabası.plaka="06 AT 45"


#ÖRNEK2
print("______ARABA 1_____")
print("Marka:{} \nRenk:{}\nPlaka:{}\nTekerlek_sayısı:{}".format(araba1.marka,araba1.renk,araba1.plaka,araba1.tekerlek_sayısı))
print("______ARABA 2_____")
print("Marka:{}\nRenk:{}\nPlaka:{}\nTekerlek_sayısı:{}".format(araba2.marka,araba2.renk,araba2.plaka,araba2.tekerlek_sayısı))
print("______EBRUNUNARABASI_____")
print("Marka:{}\nRenk:{}\nPlaka:{}\nTekerlek_sayısı:{}".format(ebrununarabası.marka,ebrununarabası.renk,ebrununarabası.plaka,ebrununarabası.tekerlek_sayısı))

#ÖRNEK3
r=float(input("Yarıçapı giriniz"))
alan=3.14*(r**2)
print("Alan:",alan)
cevre=2*3.14*r
print("Çevre:",cevre)

#ÖRNEK4
class Araba:
    marka=""
    renk=""
    plaka=""
    hiz=0

    def hizArttir(self):
        self.hiz+=10
        return self.hiz

araba1= Araba()
araba1.marka="bmw"
araba1.renk="siyah"
araba1.plaka="42 DT 06"

print("______ARABA 1______")
print("marka:{} \nrenk:{}\nplaka:{}\nhiz:{}".format(araba1.marka,araba1.renk,araba1.plaka,araba1.hiz))
araba1.hizArttir()
print("hiz:",araba1.hiz)

#ÖRNEK5
class Araba:
   # def __init__(self):
        #print("Yapıcı fonksiyon__init__()fonksiyonu çalıştı...")
    marka="FORD"
    renk="KIRMIZI"
    plaka="34 GH 100"
    hiz=20

araba= Araba()
araba2=Araba()
print("_____ARABA 1_____")
print("marka:{} \nrenk:{}\nplaka:{}".format(araba.marka,araba.renk,araba.plaka))
print("_____ARABA 2____")
print("marka:{} \nrenk:{}\nplaka:{}".format(araba2.marka,araba2.renk,araba2.plaka))


#ÖRNEK6
class Araba:
    def __init__(self, marka, renk, plaka,hiz):
        self.marka = marka
        self.renk = renk
        self.plaka = plaka
        self.hiz = hiz


araba1 = Araba("Fiat","Mavi", "25 P 45", 30)
araba2 = Araba("Bmw", "Siyah", "13 AT 43", 100)
print("____ARABA 1 _____")
print(araba1.marka)
print(araba1.renk)
print(araba1.plaka)
print(araba1.hiz)

print("_____ARABA 2_____")
print(araba2.marka)
print(araba2.renk)
print(araba2.plaka)
print(araba2.hiz)

#ÖRNEK7
class Araba:
    def __init__(self, marka="Fiyat", renk="Kırmızı", plaka="44 TT 23",hiz=30):
        self.marka = marka
        self.renk = renk
        self.plaka = plaka
        self.hiz = hiz
araba1= Araba()
print("____ARABA 1 _____")
print(araba1.marka)
print(araba1.renk)
print(araba1.plaka)
print(araba1.hiz)

#ÖRNEK 8
class Araba:
    def __init__(self, marka="Fiyat", renk="Kırmızı", plaka="44 TT 23",hiz=30):
        self.marka = marka
        self.renk = renk
        self.plaka = plaka
        self.hiz = hiz
araba1= Araba()
araba3= Araba()
araba2= Araba("Hundai","Beyaz","13 RR 23")
print("____ARABA 1 _____")
print(araba1.marka)
print(araba1.renk)
print(araba1.plaka)
print(araba1.hiz)

print("_____ARABA 2____")
print(araba2.marka)
print(araba2.renk)
print(araba2.plaka)
print(araba2.hiz)

print("_____ARABA 3_____")
print(araba3.marka)
print(araba3.renk)
print(araba3.plaka)
print(araba3.hiz)

#ÖRNEK 9
class Person:
    def __init__(self,isim,yas):
        self.isim=isim
        self.yas=yas
p1=Person("Ali",36)
print(p1.isim)
print(p1.yas)
p2=Person("Bilge",23)
print(p2.isim)
print(p2.yas)

#ÖRNEK 9 2.ÇÖZÜM
class Person:
    def __init__(self,ad=None,yas=17,gozrengi=None,notu=None):
        self.ad=ad
        self.yas=yas
        self.gozrengi=gozrengi
        self.notu=notu

    def format1(self):
        print("\n")
        print("------",self.ad,"------")
        print("yas:",self.yas)
        print("gozrengi:",self.gozrengi)
        print("notu:",self.notu)

p1=Person(ad="Ali",gozrengi="ela")
p1.format1()

p2=Person(ad="Bilge",gozrengi="yeşil",yas=19,notu=95)
p2.format1()
'''
#ÖRNEK 10
class Person:
    def __init__(mysillyobject,name,age):
        mysillyobject.name=name
        mysillyobject.age=age
    def myfunc(abc):
        print("Merhaba. Benim adım" + " "+ abc.name +" " + str(abc.age))

p1=Person("Ali",36)
p1.myfunc()
 #ÖRNEK 11
class Kullanici:
    def __init__(self,adi="Gözde",soyadi="Tez",numara=125678):
        self.adi=adi
        self.soyadi=soyadi
        self.numara=numara

    def giris(self):
        print("Giriş Yapıldı.")

    def cıkıs(self):
        print("Çıkıs Yapıldı.")

class Akademisyen(Kullanici):
    def not_ver(self):
        print("Notlarınız Pazartesi Günü Açıklanacaktır.")
class Personel(Kullanici):
    def maas_düzenle(self):
        print("Düzenlenmiştir.")
class Ogrenci(Kullanici):
    def kulube_katıl(self):
        print("Kayıt Yapılmıştır.")


akademisyen=Akademisyen("Mustafa","Kaya",125467)
personel=Personel("Mehmet","Yıldız",342563)
ogrenci=Ogrenci("Bilge","Ayvaz",234578)
print("Akademisyen")
print(akademisyen.adi)
print(akademisyen.soyadi)
print(akademisyen.numara)
akademisyen.not_ver()
print("Personel")
print(personel.adi)
print(personel.soyadi)
print(personel.numara)
personel.maas_düzenle()
print("Ogrenci")
print(ogrenci.adi)
print(ogrenci.soyadi)
print(ogrenci.numara)
ogrenci.kulube_katıl()
print("akademisyen sınıfındasınız."+ str(akademisyen.giris()))
print("akademisyen sınıfındasınız."+str(akademisyen.cıkıs()))
print("ogrenci sınıfındasınız."+str(ogrenci.giris()))
print("ogrenci sınıfındasınız."+str(ogrenci.cıkıs()))
print("personel sınıfındasınız."+str(personel.giris()))
print("personel sınıfındasınız."+str(personel.cıkıs()))
kullanici=Kullanici()
print(kullanici.giris())
print(kullanici.cıkıs())

#ÖRNEK 12

class Canli:
    def __init__(self,isim,cins,yas):
        self.isim=isim
        self.cins=cins
        self.yas=yas

    def solunum_yap(self):
        print("Solunum Yapıldı.")

    def beslenme(self):
        print("Beslenme Yapıldı.")

class Hayvan(Canli):
    evcilmi=True
    omurgalimi=True

class İnsan(Canli):
    meslek="doktor"
    def düsünür(self):
        print("İnsan düsününce var.")
    def tanit(self):
        print("Adım {},mesleğim {}".format(self.isim,self.meslek))
class Bitki(Canli):
    pass

hayvan=Hayvan("Cont","Köpek",3)
insan=İnsan("veli","erkek",20)
bitki=Bitki("nazlı","kaktüs",4)

print("HAYVAN")
print(hayvan.isim)
print(hayvan.cins)
print(hayvan.yas)

print("İNSAN")
print(insan.isim)
print(insan.cins)
print(insan.yas)
insan.düsünür()
insan.tanit()

print("BİTKİ")
print(bitki.isim)
print(bitki.cins)
print(bitki.yas)