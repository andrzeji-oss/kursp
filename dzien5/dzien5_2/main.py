# program dziekanat
# -> klasa modelu Student: index, name, lastname, grades []
# -> klasa logiki biznesowej -> addStudent(), getStudents(), deleteStudentByIndex()
# metoda uruchomieniowa -> GUI/CLI

#GUI uzytkownika

from dzien5.dzien5_2.controler.StudentController import StudentController

def commandLineInterface():
    sc = StudentController()
    while(True):
        print("Aplikacja dziekanat")
        choice = input("(I)-dodaj studenta \n(S)-wypisz studentów \n(G)-dodaj ocenę \n(D)-usuń studenta \n(Q)-wyjście")
        if(choice.upper() == "I"):
            data = input("Podaj numer indeksu, imię i nazwisko (po spacji) ").split(" ") # lista 3 elementów
            sc.addStudent(data[0], data[1], data[2])
        elif(choice.upper() == "S"):
            sc.getStudents()
        elif(choice.upper() == "G"):
            data = input("Podaj numer indeksu studenta i ocenę, którą chcesz przypisać (po spacji)").split(" ")
            sc.addGradeToStudent(data[0],float(data[1]))
        elif(choice.upper() == "D"):
            data = input("Podaj numer indeksu studenta, którego chcesz usunąć")
            sc.deleteStudentByIndex(data)
        elif(choice.upper()== "Q"):
            print("Wyjście \n")
            break
        else:
            print("Błędny wybór")

commandLineInterface()