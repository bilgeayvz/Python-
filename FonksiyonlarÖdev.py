#SORU1
'''
a=int(input("Yükseklik Giriniz:"))
b=int(input("Genişlik Giriniz:"))
def carp (a,b):
    return (a*b)
sonuc=carp(a,b)
print(sonuc)

#SORU2
sayi=int(input("Lütfen Bir sayı giriniz:"))
if sayi %2==0:
    print("Bu Bir Çift Sayıdır.")
else:
    print("Bu Bir Tek Sayıdır.")
'''
#SORU3
def fakt(x):

    return 1\
        if (x == 1 or x == 0)\
        else x * fakt(x - 1);
sayi = int(input('Lütfen Faktöriyelini Hesaplamak İstediğini Sayını Giriniz : '))
print(str(sayi) + " Sayısının faktöriyeli  =  " + str(fakt(sayi)))
