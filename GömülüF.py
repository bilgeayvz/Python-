'''
isim=["ahmet","mehmet","veli","hülya","deniz","rıza"]
maas=[13000,2000,3000,4000,5000,6000,17000,8000,9000]
zip1=zip(isim,maas)
print(list(zip1))


maas=[13000,2000,3000,4000,5000,6000,17000,8000,9000]
filter1=filter(lambda maas:maas>5000,maas)
print(list(filter1))

isim=["ahmaet","mehmet","veli","hulya","deniz","riza","remzi","ebru","naz","ceren"]
maas=[13000,2000,3000,4000,5000,6000,17000,8000,9000,10000]
yenimaas=[]
def maas1():
    for a in maas:
        if a>5000:
            yenimaas.append(a)
    print(yenimaas)
maas1()


listem=range(-5,10)
a=filter(lambda i:i>0,listem)
print(listem)
print(list(a))
'''

liste=["ali","veli","erdal","arzu"]
a=map(lambda i:i.upper(),liste)
print(list(a))

listem= [2, 4, 6, 8, 9, 10, 12, 13]
a=filter(lambda i:i>5 and i<12 ,listem)
print(list(a))

listem= [2, 4, 6, 8, 9, 10, 12, 13]

def topla(*args):
    print(sum(args))
topla(5,5,6,)


def selam(*args):
    for i in args:
        print("selam",i)
print(selam("bilge","gözde","öykü"))


def average(*args):
    av=0
    for i in args:
        av=(av+i)
        av1=av/len(args)
    print(av1)
average(3,4,2,3,2)












