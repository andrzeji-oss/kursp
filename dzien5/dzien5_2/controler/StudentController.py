# Kontroler -> klasa obsugi zadań użytkownika pochodząca z widoku (htmlk, cli, window)
# Implementuje logikę aplikacji

from dzien5.dzien5_2.model.Student import Student
from datetime import datetime

class StudentController:
    students = []

    # konstruktor - pobranie i aktualizacja listy studentów z pliku
    def __init__(self):
        inputFile = open("database.csv", "r")  # otwarcie pliku do odczytu
        for index, line in enumerate(inputFile.readlines()):
            # obsługa pierwszej linijki
            if(index == 0):
                print(line)
                continue
            # każdą linijkę z pliku mapujemy na obiekt student
            rowData = line.split(";")
            # czyszczenie ocen z []
            grades = rowData[3].replace("[","").replace("]","").split(", ")
            # konwersja ocen na float
            try:
                for index, grade in enumerate(grades):
                    grades[index] = float(grade)
            except:
                grades = []
            # utworzenie obiektu studenta na podstawie danych z jednej linii pliku
            s = Student(rowData[0], rowData[1], rowData[2], grades)
            # zapis zmapowanego obiektu do listy students
            self.students.append(s)
        inputFile.close()

    # metoda dodająca studenta do listy
    def addStudent(self, index, name, lastname):
        if(self.validateStudentIndex(index)):
            # utworzenie obiekty studenta -> odwołanie do modelu
            s = Student(index, name, lastname)
            self.students.append(s)
            print("Dodano: ", s)
        else:
            print("Istnieje student o takim indexie")

    # metoda do walicacji danych studenta
    def validateStudentIndex(self, inputIndex):
        for student in self.students:
            if(student.index == inputIndex):
                # jezeli wystepuje taki index
                return False # dodajemy do listy
        return True # nie dodajemy do listy

    #metoda dodająca ocenę
    def addGradeToStudent(self, inputIndex, grade):
        gradesTemplate = [2,3,3.5,4,4.5,5,5.5]
        if (grade in gradesTemplate):
            isAdded = False
            for student in self.students:
                if(student.index == inputIndex):
                    isAdded = True
                    student.addGrade(grade)
                    print("Dodano ocenę")
                #wypisz zaktualizowaną lista studentów
            if(isAdded == False):
                print("Nie ma studenta o takim indeksie")
            self.getStudents()
        else:
            print("Podałeś niepoprawną ocenę")

    def deleteStudentByIndex(self, inputIndex):
        for student in self.students:
            if(student.index == inputIndex):
                print("Usunięto ", student)
                self.students.remove(student)
        self.getStudents()

    # metoda wypisująca wszystkich studentów z listy studentów
    def getStudents(self):
        print("| %6s | %15s | %15s | %20s| %7s |" % ("INDEKS", "IMIĘ", "NAZWISKO","OCENY", "ŚREDNIA"))
        for student in self.students:
            print(student)

    def __del__(self): #destruktor wywołuje się automatycznie gdy niszczony jest obiekt z pp
        outputFile = open("database.csv","w")
        # podanie czasu ostatniego zapisu
        outputFile.write("Ostatnia aktualizacja: " + str(datetime.now()) + "\n")
        # aktualizacja zawartości pliku
        for student in self.students:
            outputFile.write(student.index + ";" + student.name + ";" + student.lastname + ";" + str(student.grades) + ";" + str(student.calculateAVG()) + "\n")
        # zamknięcie strumienia danych
        outputFile.close()

#sc = StudentController()
#sc.addStudent(123456, "test", "test")
#sc.addStudent(654321, "test1", "test1")

#sc.addGradeToStudent(123456,5)
#sc.addGradeToStudent(123456,3)
#sc.addGradeToStudent(654321,2)
#sc.addGradeToStudent(123452,5)

#sc.getStudents()

#sc.deleteStudentsByIndex(123456)