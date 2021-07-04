
# ICINDEKILER;
# class
# __init__
# self
# __str__
# __eq__
# inheritance
# super()
# polymorphism
# private
# decorator setter and getter


# position,name,age,level,salary
se1 = ['Software Engineer','Max',20,'Junior',5000]
se2 = ['Software Engineer','Lisa',25,'Senior',7000]

# class buyuk harfle yazilir
# bir objeyi tanimlamak icin __init__ kullanilir
# her obje tanimlamasinda self kullanilir. self ile objenin tum nitelikleri birlestirilir
class SoftwareEngineer:
    def __init__(self,name,age,level,salary):
        self.name = name
        self.age = age
        self.level=level
        self.salary=salary

    def __str__(self):
        information = f"name= {self.name},age= {self.age},level={self.level}"
        return information

    def __eq__(self,other):
        return self.name==other.name and self.age==other.age and self.salary==other.salary

se1 = SoftwareEngineer('Max',20,'Junior',5000)
print(se1.name)

print(se1)
# yukaridaki print kodunu calistirdiginda sana ogjeyle ilgili gereksiz bilgileri verir.(yukarida __str__  kismini comment yapmalisin calistirmadan once)
# eger objenin kendisinin bilgilerini istiyorsan __str__ metodunu kullanmalisin
# simdi ayni ozelliklere sahip bir nesne daha tanimlayalim
se2 = SoftwareEngineer('Max',20,'Junior',5000)
print(se1==se2)
# sonucu false olarak verdi halbuki ayni obje olarak tanimlamistik(yukarida __eq__ kismini comment yapmalisin calistirmadan once)
# cunku memory adreslerini karsilastirdi
# eger dogru karsilastirma yapmak istiyorsak __eq__ metodunu kullanmaliyiz.

# diyelim ki SoftwareEngineer ile Designer class larimiz var.
# fakat br class daha var ki(Employee) bu iki class i da kapsiyor.
# iste bunu ifade edebilmek icin inheritance kullaniriz.
class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Softwareengineer(Employee):
    pass

class Designer(Employee):
    pass
# parantez icinde Employee yazarak ana class i parantez icine yazdik.
# Boylece tum Softwareengineer ve Designer class lari ayni zamanda Employee class inin icinde bulunacak.

# ornegin yukarida Softwareengineer class inin icini bos biraktik ama ana class in(Employee) icini doldurduk.
# simdi yeni bir nesne eklemeye calisalim bakalim ici bos olmasina ragmen calisiyor mu?
se = Softwareengineer('deniz',26)
print(se.name,se.age)
#goruldugu uzere ana classtaki ifadeleri aldi ve calisti.
# ben Softwareengineer classinin icerisine ana classtakinden farkli nitelikler de koymak istiyrsam;
class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Softwareengineer(Employee):
    def __init__(self,name,age,level,salary):
        super().__init__(name,age)  # burada ana class ismini yazmak yerine super() metodunu kullandik
        self.level = level
        self.salary = salary

    def work(self):
        print(self.name + " is coding")


class Designer(Employee):
    def work(self):
        print(self.name + " is drawing")


employees = [Softwareengineer('deniz',26,'junior',5000),
            Designer('elif',30)]


def mot_employee(employees):
    for employee in employees:
        employee.work()

mot_employee(employees)
# yukarida yaptigim bu ornekte kod ayni olmasina ragmen her sinif icin kendine ozgu cikti verdi
# iste buna polymorphism denir


# diyelim ki SoftwareEngineer class inin icine tanimladigin salary degiskenini kimsenin gormesini istemiyorsun(private) kodu erisen kisiden baska;
class Softwareengineer:
    def __init__(self,name,age,level):
        self.name = name
        self.age = age
        self.level = level
        self._salary = 5000

se = Softwareengineer('deniz',26,'junior')
print(se.name,se.age, se._salary)
# goruldugu uzere kodu yazan kisi salary degiskenine erisebiliyor. Fakat disaridan biri erisim saglayamiyor.
# eger kodu yazan kisiye de bu nitelik gizli olsun istiyorsan;
class Softwareengineer:
    def __init__(self,name,age,level):
        self.name = name
        self.age = age
        self.level = level
        self.__salary = 5000

se = Softwareengineer('deniz',26,'junior')
print(se.name,se.age, se.__salary)
# 2 tane alt cizgi kullandik tamamen gizli olsun diye.

# simdi decorator kullanarak salary niteligine nasil ulasilir ya da nasil tanimlanir ona bakalim;
class Softwareengineer:
    def __init__(self):
        self._salary = None

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,value):
        self._salary = value

    #@salary.deleter
    #def salary(self):
        #del self._salary

se = Softwareengineer()
se.salary=5000
print(se.salary)
