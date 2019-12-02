# program dziekanat
# #wczytuje od uzytkowniak kolejne oceny
# [3-5]
#wyswietla srednia arytmetyczna

def isGrade(grade):
    return grade in gradesTemplate

def gradesAvg(grades):
    return


gradesTemplate = (3.0, 3.5, 4.0, 4.5, 5.0)
grades = []

while(True):
    grade = input("Wprowadź ocenę lub ENTER aby zakończyć  ")
    if(grade == ""):
        print("Koniec")
        break

    try:
        grade = float(grade)
    except:
        print("Ocena musi być liczbą 3.0")

    if not isGrade(grade):
        print("nie ma takiej oceny")
        continue
    grades.append(grade)

print("Wprowadzone oceny: " + grades)