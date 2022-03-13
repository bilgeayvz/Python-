'''
#Örnek 1
for sayilar in range (20,5,-3):
    print(sayilar)

#Örnek 2
for sayilar in range(10):
    print(sayilar)
else:
    print("Döngü Bitti")

#Örnek 3
#For döngüsü ile 1 den 10 a kadar olan sayıların toplamı
toplam=0
for sayi in range(1,11)
    toplam=toplam+sayi
print(toplam)
#Örnek 4
meyveler=["çilek","muz","şeftali"]
for meyve in meyveler:
    print(meyve)

#Örnek5
for harfler in "Döngü":
    print(harfler)

#Örnek6
sayilar=[10,11,12,13,14,15,16,17,18,19,20]
for sayi in sayilar:
    if sayi%3==0:
        print(sayi)

#Örnek7
#5 ten geri sayıp ateşleme yapan programı for döngüsüyle yazalım
for i in [5,4,3,2,1]:
    print(i)

#Örnek8
print("ATEŞ!!")
friends=["Ahmet","Ayşe","Hüseyin"]
for friend in friends:
    print("mutlu yıllar:",friend)
print("Bitti")

#### iterasyon değişkeni=i

#Örnek9
print('ONCE')
for thing in [9,41,45,81,90]:
    print(thing)
print("SONRA")

#Örnek10
print("The break instruction:")
for i in range(1,6):
    if i==3:
        break
    print("Inside the loop.",i)
print("Outside the loop.")
print("\nThe continue instruction:")
for i in range (1,6):
    if i==3:
        continue
    print("Inside the loop.")
print("Outside the loop.")

#Örnek11
i=0
while (i<5):
    print("kodlama")
    i=i+1

#Örnek12
n=5
while n>0:
    print(n)
    n=n-1
print("Ateş!")

#Örnek13
i=0
while(i<=20):
    print(i)
    i=i+2
print("Döngü Sonu")

#Örnek14
i=1
sonuc=1
faktoriyel=int(input("Faktöriyel hesaplancak sayıyı giriniz:")
while (i<=faktoriyel):
     sonuc=i*sonuc
     i=i+1
print("sonuc:",sonuc)

#Örnek15
toplam=0
sayi=1
while(sayi!=0):
    sayi=int(input("Bir sayı giriniz:"))
    toplam=toplam+sayi
print("Sonuc:",toplam)


#Örnek16(iç içe döngü)
for i in range(0,3):
    for j in range(0,3):
        print([i,j])

#Örnek17
i=0
while True:
    if(i==5):
        print("Döngüden Çıkıldı.")
        break
    print(i)
    i=i+1

#Örnek18
sayi=int(input("Bir sayı giriniz:"))
for i in range(1,10):
    if i==sayi:
        break
    print(i)
print("Döngü sona erdi")


#Örnek 19
metin="Ankara"
for i in metin:
    if i=='r':
        break
    print(i)

#Örnek20
toplam=0
sayi=1
while sayi>=0:
    sayi=int(input("Sayıyı giriniz:"))
    if sayi<0:
        break
    else:
        toplam=toplam+sayi
        print("Toplam=",toplam)
print("Döngü Sonlandı.")

#Kullanıcıdan isim isteyin ismi 5 kere yan yana yazsın.
#Örnek
ad=input("isminizi girin:")
for i in range(1,6):
    print(ad,end="")

print içerisinde atama operatörü kullanılmaz.
#Örnek
name=input("Enter your name:")
for harf in name:
    print(harf)

#Çözümyolu1
isim=input("isminizi giriniz:")
a=len(isim)
for i in range(1,a+1):
    b=isim[a-i]
    print(b,end="")
#Çözümyolu2
name=input("isim")
ters=""
for i in range(len(name),0,-1):
    ters+=name[i-1]
print(ters)


#Örnek
sayac=0
sayi=input('Bir Sayı Giriniz: ')
for i in range(2,int(sayi)):
  if(int(sayi)%i==0):
    sayac+=1
    break
if(sayac!=0):
  print("Girilen Sayı Asal Değil")
else:
  print("Girilen Sayı Asal")

#Örnek
for i in range(1,11):
    for j in range(1,11):
        print(i, "x", j, "=", i * j)
    print("________"*3)

#Örnek
gizliSayi=77
for hak in range(1,6):
   tahmin=int(input("Sayıyı tahmin et:"))
   if tahmin==gizliSayi:
       print("Tebrikler!")
       break
   elif tahmin<gizliSayi:
       print("Benim sayım daha büyük.")
   else:
       print("Benim sayım daha küçük.")
else:
    print("Bulamadınız sayım:",gizliSayi)
'''

sayilar=[10,23,-5,0,4,-8,-1,3,-9]
toplam=0
negatifSayilar=0
for sayi in sayilar:
    if sayi>0:
        toplam=toplam+sayi
    elif sayi<0:
        negatifSayilar=negatifSayilar+1
print("pozitif sayıların toplamı:",toplam)
print("Negatif sayıların sayısı:",negatifSayilar)








