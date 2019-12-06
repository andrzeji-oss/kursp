from dzien6.pracownicy.model.Employee import Employee, Permission
from dzien6.pracownicy.model.Trainee import Trainee
import hashlib


class CompanyController:
    employees = [
        Employee("mk1","mk1","PYTHON DEV",11000,Permission.ROLE_EMPL),
        Employee("mk2","mk2","JAVA DEV",9000,Permission.ROLE_EMPL),
        Employee("mk3","mk3","PYTHON DEV",12000,Permission.ROLE_EMPL),
        Employee("mk4","mk4","MANAGER",14000,Permission.ROLE_MAN),
        Employee("mk5","mk5","SCRUM MASTER",13000,Permission.ROLE_MAN),
        Employee("mk6","mk6","HEAD",17000,Permission.ROLE_HEAD),
        Employee("mk7","mk7","HEAD",21000,Permission.ROLE_HEAD),
        Employee("mk8","mk8","DEV OPS",11500,Permission.ROLE_EMPL),
        Trainee("t1", "t1"),
        Trainee("t2","t2"),
        Trainee("t3","t3")
    ]
    #1. dodawanie pracownika lub praktykanta z unikatowym loginem
    def addEmployeeOrTrainee(self, o):
        if(o.__class__.__name__ == "Trainee" or o.__class__.__name__ == "Employee"):
            if(self.loginValid(o.login)):
                print("Dodano pracownika", o.login, o.possition)
                self.employees.append(o)
            else:
                print("Istnieje już taki login w bazie danych")
        else:
            print("Dany obiekt nie jest pracownikiem ani praktykantem")

    # sprawdzenie czy dany login nie istnieje w liście employees
    def loginValid(self, login):
        for e in self.employees:
            if(e.login == login):
                return False
        return True

    #2. wyświetlenie wszystkich pracowników i praktykantów posortowanych po pensji DESC
    def getEmployees(self):
        for e in sorted(self.employees, key=lambda e : e.salary, reverse=True):
            print(e)

    #wyświetlenie tylko kierowników lub dyrektorów po loginie A-Z
    def getManagersAndHeadsOrderByLoginASC(self):
        # filtruję listę pracowników i zwraca kierowników i dyrektorów
        result = filter(lambda i : i.__class__.__name__ == "Employee" and i.permission.value in [2,3], self.employees)
        for i in sorted(result, key=lambda i : i.login, reverse=False):
            print(i)
        # for e in self.employees:
        #     if(e.__class__.__name__ == "Employee"):
        #         if(e.permission.value in [2,3]):
        #             print(e)

    #wyświetlenie tylko praktykantów Z-A
    def getTraineeOrderByLogin(self):
        # filtruję listę pracowników i zwraca tylko praktykantów
        result = filter(lambda t : t.__class__.__name__ == "Trainee", self.employees)
        for t in sorted(result, key=lambda t : t.login, reverse=True):
            print(t)

    # przypisanie nagrody do pracownika lub praktykanta, jeżeli nie podajemy loginu to premia dla wszystkich
    def setPreise(self, amount, login = ""):
        if (login != ""):
            islogin = False
            for e in self.employees:
                if(e.login == login):
                    e.assignPrise(amount)
                    islogin = True
                    break
            if(islogin == False):
                print("Błędny login pacownika")
        else:
            for e in self.employees:
                e.assignPrise(amount)
        self.getEmployees()


    # zmiana pensji tylko dla pracownika
    def changeEmployeeSalary(self, login, salary):
        isEmployee = False
        for e in self.employees:
            if(e.login == login and e.__class__.__name == "Employee"):
                e.salary = salary
                isEmployee = True
                break
        if(isEmployee == False):
            print("Błędny login lub typ pracownika")
            self.getEmployees()

    # usuwanie pracownika lub praktykanta z listy
    def deleteEmployeewithConfirm(self, login):
        isFound = False
        for e in self.employees:
            if(e.login == login):
                isFound = True
                inputPasswd = input("Potwierdź usuwanie hasłem").strip(" ")
                if(e.password == hashlib.md5(("salt:XYZ"+inputPasswd).encode('utf-8')).hexdigest()):
                    self.employees.remove(e)
                    print("Usunięto: ", e.login)
                else:
                    print("Błąd potwierdzenia")
        if(isFound == False):
            print("Nie ma takiego pracownika")
        self.getEmployees()

cc = CompanyController()
cc.getEmployees()