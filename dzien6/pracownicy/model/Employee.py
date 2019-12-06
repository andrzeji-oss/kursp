from dzien6.pracownicy.model.Trainee import Trainee
from enum import Enum

class Permission(Enum):
    ROLE_EMPL = 1
    ROLE_MAN = 2
    ROLE_HEAD = 3

class Employee(Trainee):
    def __init__(self, login, password, possition, salary, permission = Permission.ROLE_EMPL):
        super().__init__(login, password)
        self.possition = possition
        self.salary = salary
        self.permission = permission

    def __str__(self):
        return super().__str__() + " %15s |" % (self.permission.value)

# e = Employee("mk", "mk", "PYTHON DEV", 10000)
# e1 = Employee("mk1", "mk1", "PYTHON_DEV", 11000, Permission.ROLE_MAN)
# e.assignPrise(5000)
#
# print(e)
# print(e1)


