# zwraca wszystkie elementy tablicy, ktore sa wieksze od wartosci j
# uzytkownik podaje wartosc progu minsup i ilosc genereowanych elementow tablicy
# elementy talicy przy kazdym uruchomieniu programu sa generowane losowo z zakresu -1000, 1000
# funkcja ma zwrocic elementy wieksze od wartosci progowej oraz wartosc ich sumy

from random import randint
def generateNRandomElements(n):
    elements =[]
    for i in range(n):
        elements.append(randint(-1000,1000))
    return elements

def getElementsSupportTreshold(n, treshold):
    elementsSupportTreshold = []
    cumSum = 0
    for elem in generateNRandomElements(n):
        if (elem > treshold):
            cumSum += elem
            elementsSupportTreshold.append(elem)
    return elementsSupportTreshold,cumSum

print(getElementsSupportTreshold(100,0))