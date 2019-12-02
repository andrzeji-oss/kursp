# funkcja zwracajaca kolejna liczbę pierwszą

def getprimaryNumbers(n):           #mozna podac w funkcji argument domyślny
    primaryNumbers = [1]
    number = 2
    while(len(primaryNumbers) < n):
        isPrimary = True
        for div in range (2, number):
            if(number % div == 0):
                isPrimary = False
        if(isPrimary):
            primaryNumbers.append(number)
        number += 1
    return primaryNumbers, primaryNumbers[len(primaryNumbers) -1]

element = 10
print("Lista: ", getprimaryNumbers(element)[0])
print("N-ty element: ", getprimaryNumbers(element)[1])

from datetime import date

def printParameters(login, password, email, status=True, registratetionDate=date.today()):
    return ("%s %s %s %s %s" % (login, password,email,status,registratetionDate))

print(printParameters("ai", "as", "ai"))

def nonDefinedParameters(*elements):
    sum = 0
    for elem in elements:
        sum += elem
    return sum/len(elements)

print(nonDefinedParameters(1))
print(nonDefinedParameters(4,5,6))
print(nonDefinedParameters(23435,3 ,343, 43, 43, 4))

def sortList(numbers):
    numbers.sort()
    return numbers
list = [3,2,5,4,6]
print(sortList(list))