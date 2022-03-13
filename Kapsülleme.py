class RegisterCourse:
    def __init__(self):
        self.name="Bilge"
        self.surname="Ayvaz"
        self.__exam1=86 #class dışından erişilemiyor(__ koyunca)
        self.exam2=90
        self.courses=[]
    def add(self,course):
        self.courses.append(course)


register=RegisterCourse()
register.exam1=75 #class içerisinde değerini değiştiriyoruz.

register.add("Veri Bilimi")
register.add("Python Eğitimi")
print("isim:",register.name)
print("soyisim:",register.surname)
print("Exam1:",register.exam1)
print("Exam2:",register.exam2)
print(register.courses)

#Kapsülleyerek erişime izin verme.*****private*****
class RegisterCourse:
    def __init__(self):
        self.name = "Bilge"
        self.surname = "Ayvaz"
        self.__exam1 = 86
        self.__exam2 = 90
        self.courses = []

    def __add(self, course):
        self.courses.append(course)


register = RegisterCourse()

register.add("Database Managment") #Fonksiyonu çağırma.




