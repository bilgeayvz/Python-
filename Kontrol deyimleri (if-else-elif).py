
#ÖRNEK1
yas=int(input("yaşınızı girin:"))
if yas>=18:
    print("Mekana Girebilirsin!")
else:
    print("Mekana Giremezsin!")
#ÖRNEK 2
yıl=int(input("Yıl giriniz:"))
if yıl %4 ==0:
    print("Bu bir yıl")
else:
    print("Bu bir yıl değil")

#ÖRNEK3
x=5
y=10
z=8
print(x>y)
print(y>z)

x=10
if x == 10:
    print(x==10)
if x>5:
    print(x>5)
if x<10:
    print(x<10)
else:
    print("else")

#ÖRNEK4
x=1
y=1.0
z="1"
if x==y:
   print("one")
if y==int(z):
    print("two")
elif x==y:
    print("three")
else:
    print("four")

#ÖRNEK5
sayi1=int(input("sayı1 girin:"))
sayi2=int(input("sayı2 girin:"))
if sayi1<sayi2:
    print("sayi1<sayi2")
    print(sayi1, "<" ,sayi2)
else:
    print("sayi1>sayi2")
    print(sayi1,">",sayi2)

#ÖRNEK6
sayi1=int(input("sayi1 giriniz:"))
sayi2=int(input("sayi2 giriniz:"))
ortalama=(sayi1+sayi2)/2
print("ortalama",ortalama)
if sayi1<30 or sayi2<30:
    print("kaldı")
else:
    if ortalama >=50:
        print("geçti")
    else:
        print("kaldı")

#ÖRNEK7
yil=int(input("yıl giriniz:"))
if yil %4==0:
    print("366 gün")
else:
    print("365 gün")

#ÖRNEK8
sayi1 = int(input("1. Sayı: "))
sayi2 = int(input("2. Sayı: "))
sayi3 = int(input("3. Sayı: "))

if (sayi1 >= sayi2) and (sayi1 >= sayi3):
    buyuk = sayi1
elif (sayi2 >= sayi1) and (sayi2 >= sayi3):
    buyuk = sayi2
else:
    buyuk = sayi3

print(sayi1, ",", sayi2, "ve", sayi3, "içinde büyük olan sayı", buyuk)
print(sayi1, ",", sayi2, "ve", sayi3, "içinde büyük olan sayı", buyuk)
