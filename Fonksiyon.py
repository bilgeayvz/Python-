'''
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


def hello (isim,yas):
    print("merhaba",isim,yas)
isim=input("İsminizi giriniz:")
yas=int(input("Yaşınızı giriniz:"))
hello(isim,yas)
'''
#import random

'''
def alan(r):
    return 3.14*r**2
def cev(r):
    return 2*3.14*r
a=int(input("capi:"))
print("alan=",alan(a))
print("cevre=",cev(a))
'''

a=int(input("Yükseklik Giriniz:"))
b=int(input("Genişlik Giriniz:"))
def carp (a,b):
    return (a*b)
sonuc=carp(a,b)
print(sonuc)

sayi=int(input("Lütfen Bir sayı giriniz"))
if sayi %2==0:
    print("Bu Bir Çift Sayıdır.")
else:
    print("Bu Bir Tek Sayıdır.")

def r(a,b,c):
    z=a+b*c**2
    return z
a=int(input("enter A:"))
b=int(input("enter B:"))
c=int(input("enter C:"))
print(r(a,b,c))
