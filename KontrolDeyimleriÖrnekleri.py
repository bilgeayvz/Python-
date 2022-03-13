'''
#ÖRNEK 1
defislemci="i7"
defram="8gb"
islemci=input("işlemci giriniz:")
ram=input("ram giriniz:")
if((defislemci==islemci) or(defram!=ram)):
    print("Kurulum uygun")
elif((defislemci!=islemci) or(defram==ram)):
    print("kurulum uygun")
else:
    print("kurulum uygun değil")

#ÖRNEK 2
sayi1=int(input("1.sayıyı giriniz:"))
sayi2=int(input("2.sayıyı giriniz:"))
op=input("yapılacak işlemi(+ - * /) giriniz:")

if op=="+":
    print(sayi1+sayi2)
elif  op=="-":
    print(sayi1-sayi2)
elif op=="*":
    print(sayi1*sayi2)
elif op=="/":
    print(sayi1/sayi2)
else:
    print("yanlış işlem girdiniz")

#ÖRNEK 3
hava=int(input("Bir derece giriniz:"))
if hava>=0 and hava<=5:
    print("Hava soğuk")
elif hava>=6 and hava<=14:
    print("Hava ılık")
elif hava>=15:
     print("Hava sıcak")
else:
    print("Lütfen geçerli bir derece girin.")

#ÖRNEK 4
agirlik=int(input("Ağırlığınızı girin:"))
boy=float(input("Boyunuzu girin:"))
vki=agirlik/(boy*boy)
print(vki)
if vki>=18 and vki<=25:
    print("normal")
elif vki>=26 and vki<=55:
    print("normal üstü")
elif vki>=56 and vki<=70:
    print("obez")
else:
    print("Aralık dışı")

#ÖRNEK 5
sayi1=float(input("sayi1 giriniz:"))
sayi2=float(input("sayi2 giriniz:"))
sayi3=float(input("sayi3 giriniz"))
ortalama=(sayi1+sayi2+sayi3)/3
print("ortalama",ortalama)
if ortalama<=50:
    print("Kaldınız")
elif ortalama>=50:
    print("Geçtiniz")

#ÖRNEK 6
vize_notu = float(input("Vize notu gir : "))
final_notu = float(input("Final notu gir :"))
gecme_notu=(0.4*vize_notu)+(0.6*final_notu)
print("geçme notu",gecme_notu)
if gecme_notu >60:
 print("Geçtiniz")
else:
    print("Kaldınız")
'''


#ÖRNEK 7

vize_notu = float(input("Vize notu gir : "))
final_notu = float(input("Final notu gir :"))
ortalama_not = (0.4 * vize_notu) + (0.6 * final_notu)
print("Not ortalamanız : ", ortalama_not)
if ortalama_not >= 60 and float(final_notu)>=60:
    print("geçtiniz")
else:
    print("kaldınız")

#ÖRNEK 8
sayi=int(input("Bir sayı giriniz:"))
if sayi>=1 and sayi<=100:
    print("Doğru sayı girişi")
else:
    print("Hatalı giriş")

parola=input("parola gir:")
uzunluk=len(parola)
print(len(parola))
if uzunluk<8:
    print("parolanız zayıf")
else:
    print("güçlü parola")

