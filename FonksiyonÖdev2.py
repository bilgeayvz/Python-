'''
#SORU1
def a(x):
    if 0<=x<=50:
        return 1
    elif 50<x<=60:
        return 2
    elif 60<x<=70:
        return 3
    elif 70<x<=85:
        return 4
    elif 85<x<100:
        return 5
    else:
        return "yanlis girdiniz"
x=int(input("puan yazin"))
print(a(x))

#SORU2
def r(x,y):
    return (x+y)/2
x=float(input("baslangic sayisi "))
y=float(input("bitis sayisi "))
print("ortalama",r(x,y))

a=int(input("başlangıç değerini giriniz."))
b=int(input("bitiş değerini giriniz."))

if a>b:
    a,b=b,a

print(a,b)

while a==b:
    print("hatalı giriş yaptınız. tekrar giriş yapın.")
    a=int(input("başlangıç değerini giriniz."))
    b=int(input("bitiş değerini giriniz."))

c=list(range(a,b))
print(c)

s=list(filter(lambda x:x%2==0,c))
print(s)

toplam=reduce(lambda x,y:x+y,s)
print(toplam)
print(toplam/len(s))

def s(a,b):
    return a[b]+a[b-1]
a=[0,1]
x=1
while a[x]<610:
    a.append(s(a,x))
    x+=1
print(a)
'''
from functools import reduce


def mukemmelsayı(x):
    list1=[]
    for i in range(1,x):
        if x%i==0:
            list1.append(i)
    toplam= reduce(lambda x,y:x+y,list1)
    print(list1)
    print(toplam)
    if toplam==x:
        print("mükemmel sayı")
    else:
        print("mükemmel sayı değil")

a=int(input("mükemmel sayı mı"))
mukemmelsayı(a)


challenge: a=int(input("başlangıç değerini giriniz."))
b=int(input("bitiş değerini giriniz."))
max=(a+b+abs(a-b))/2
print("büyük sayı",max)
min=(a+b-abs(a-b))/2
print("küçük sayı",min)
a=int(input("sayı giriniz."))
b=int(input("sayı giriniz"))
max=(a+b+abs(a-b))/2
print("büyük sayı",max)
min=(a+b-abs(a-b))/2
print("küçük sayı",min)
