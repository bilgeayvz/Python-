'''
metin=input("içeriği yazınız:")
sayac=0
for i in metin:
    if i==" ":
        sayac=sayac+1
print("Kelime sayısı",sayac+1)

#return fonsiyonun çağrıldığı yere değer götürmesi
import random
liste=set()
sayi=0
while len(liste)<10:
    sayi=random.randint(0,100)
    liste.add(sayi)
print(liste)

a=20
b=5
def toplama(a,b):
    return(a+b)
def carp(a,b):
    return(a*b)
def cikar(a,b):
    return(a-b)
def bol(a,b):
    return(a/b)
sonuc=toplama(a,b)
sonuc1=carp(a,b)
sonuc2=cikar(a,b)
sonuc3=bol(a,b)
print(sonuc,sonuc1,sonuc2,sonuc3)
'''

def hello (isim,yas):
    print("merhaba",isim,yas)
isim=input("İsminizi giriniz:")
yas=int(input("Yaşınızı giriniz:"))
hello(isim,yas)





