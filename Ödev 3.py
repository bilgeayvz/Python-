a=int(input("Lütfen bir sayı giriniz [0-100]:"))
if a>=80:
    if a>=96:
        print(100)
    elif a>=100:
        print("Hata")
    else:
        a+=10
        print(a)
elif a>=60 and a<80:
    a+=5
    print(a)
elif a>=46 and a<=59:
    print("Bu aralıkta puan eklemesi ve çıkarması yok")
elif a <= 45:
    if a==4:
        print(0)
    else:
        a-=5
        print(a)
