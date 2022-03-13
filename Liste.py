#Append listenin sonuna eleman eklemek için kullanılır.
#extend listeleri birleştirmek için kullanılır.
#ınsert istedğin yere ekleme yapar.
#remove listenin içinden değeri verilen elemanı siler
#pop istediğin elemanı siler
#clear listededeki tüm elemanları siler
#ındex listede ki konumunu bulur
#count belirtilen elemandan kaç adet olduğunu belirtir.
#sort listenin içindeki elemanları sıralar veri tiplerine uygun sıralanır.
#reverse listeyi ters yazar
#copy listeyi yeni bir liste olarak kopyalar
#del indeksi verilen elemanı siler.pop fonksiyonun benzer bir fonksiyon olmasına rağmen kullanımı farklıdır.
'''
takimlar=["gs","fb","bjk"]
takimlar.append("ts")
print(takimlar)

sebzeler=["lahana","pırasa","ıspanak","fasulye"]
sebzeler.remove("ıspanak")
sebzeler.insert(2,"patlıcan")
print(sebzeler)

iller1=["Ankara","İstanbul","Amasya","Kahramanmaraş"]
iller2=[]
iller2=iller1.copy()
print(iller2)

takimlar=["GS","FB","BJK","TS","FB","FB"]
sayi=takimlar.count("FB")
print(sayi)

sehir1=["Ankara","Artvin","Amasya","Ağrı"]
sehir2=["Burdur","Balıkesir","Bursa"]
sehir1.extend(sehir2)
print(sehir1)
sehir2.sort()
print(sehir2)

sebzeler=["Lahana","Marul","Pırasa","Ispanak","Fasulye"]
sebze=sebzeler.index("Ispanak")
print(sebze)
iller=["sivas","samsun","sakarya","sinop","adana","ankara"]
il=iller.index("adana")
print(il)

liste1=[1,2,3,4,5]
liste2=[2,3,4,5]
liste1=liste2
print(liste1)

araba=["Bmw","Mercedes","Opel","Mazda"]
araba[-1]="toyota"
print(araba)

araba=["BMW","Mercedes","Opel","Mazda"]
print("Mercedes"in araba)


araba=["BMW","Mercedes","Opel","Mazda"]
print(araba[-2])

araba=["BMW","Mercedes","Opel","Mazda"]
print(araba[:3])

araba=["BMW","Mercedes","Opel","Mazda"]
araba[-2:]="Toyota","Renault"
print(araba)

araba=["BMW","Mercedes","Opel","Mazda"]
araba1=["Audi","Nissan"]
araba.extend(araba1)
print(araba)

araba=["BMW","Mercedes","Opel","Mazda"]
del araba[-1]
print(araba)

araba=["BMW","Mercedes","Opel","Mazda"]
araba.reverse()
print(araba)

liste=["ağaç","yaprak","toprak","su","ateş"]
liste.clear()
print(liste)

sebzeler=["lahana","marul","pırasa","ıspanak","fasulya"]
sebzeler.pop(2)
print(sebzeler)

liste1=[1,3,5,7,9]
liste2=[0,2,4,6,8]
liste1.append(liste2)
print(liste1)
print(len(liste1))

liste1=[1,3,5,7,9]
liste2=[0,2,4,6,8]
liste1.extend(liste2)
liste1.sort()
print(liste1)

#tuple (demet) veri tipi
#list-tupple-dictionary


pd=('python','c++','java')
print(pd)
'''
#add(tek eleman eklemek için) update(birden fazla eleman eklemek için)
#silmek için remove ve discard{}
dersler=("Python","C++ Dersleri","Java","C++ Dersleri")
dersler_liste=list(dersler)
dersler_liste[2]='c++'
print(dersler_liste)

dersler=("Python","C++ Dersleri","Java","C++ Dersleri")
print(len(dersler))









