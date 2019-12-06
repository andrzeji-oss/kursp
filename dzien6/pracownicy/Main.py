from dzien6.pracownicy.controler.CompanyController import CompanyController
from dzien6.pracownicy.model.Employee import Employee
from dzien6.pracownicy.model.Trainee import Trainee

cc = CompanyController()
# cc.addEmployeeOrTrainee(Employee("e1","e2","Junior DEV", 5000))
# cc.addEmployeeOrTrainee(Employee("e1","e2","Junior DEV", 5000))
# cc.addEmployeeOrTrainee("Pani Jadzia z gazowni")
# cc.addEmployeeOrTrainee(Trainee("p1","p2"))
# cc.getEmployees()
# cc.getTraineeOrderByLogin()
# cc.getManagersAndHeadsOrderByLoginASC()
# cc.setPreise(100, "t1")
cc.deleteEmployeewithConfirm("t1")