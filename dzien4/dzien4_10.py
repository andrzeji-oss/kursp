from datetime import date

class User:
    def __init__(self, login,password, status, registrationDate): #metoda wywolania
        # pole klasowe są inicjalizowane wartościami z argument funkcji
        self.login = login
        self.password = password
        self.status = status
        self.registrationDate = registrationDate

    def setStatus(self, status): #modyfikacja statusu na wartość podaną w argumencie
        lista = ["a", "b", "c"]
        self.status = status

    def __str__(self): #funckja wywołujaca gdy obiekt jest rzutowany do napisu
        return ("| %10s | %10s | %8s | %10s |" % (self.login, self.password, self.status, self.registrationDate))

    def __del__(self):
        print("obiekt %s jest usunięty" % (self))

u1 = User("ai@ai.pl", "ai", True, date.today())
print(u1.login, u1.password, u1.status, u1.registrationDate)

u2 = User("bb@bb.pl", "bbi", False, date.today())
print(u2.login, u2.password, u2.status, u2.registrationDate)

u3 = User("bb@bb.pl", "bbi", False, date.today())
print(u3.login, u3.password, u3.status, u3.registrationDate)
u3 = u2

u1.status = False

print(u1)
print(u2)
print(u3)


print(u1.__class__.__name__)
print(type(u1))

u4 = User("x", "x", True)
u5 = User("x", "x", True, registrationDate="2000-02-02")
print(u4)
print(u5)

print(u5.__del__())
print(u5)