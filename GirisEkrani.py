ad = "bilvz"
sifre = "12345"

while True:
    kullanici = input("Kullanıcı adınızı giriniz: ")
    parola = input("Şifrenizi giriniz: ")
    if kullanici == ad and parola == sifre:
        print("Giriş Başarılı Hoşgeldiniz")
        break
    elif kullanici == ad and parola != sifre:
        print("Şifreniz yanlış\n")
    elif kullanici != ad and parola == sifre:
        print("Kullanıcı adınız yanlış \n")
    else:
        print("Kullanıcı adı ve şifre hatalı\n")