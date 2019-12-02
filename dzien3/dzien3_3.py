# wygeneruj 100 elementową tablice z randomowymi wartościami 1-100

# utwórz listę wartości
import random

randomList = []
count = 0

liczba = int(input("Podaj liczbę z zakresu 1-10:"  ))

for i in range(100):
    randomList.append(random.randint(1,10))
print(randomList)

if(liczba not in randomList):
    print("Element %i nie występuje w liście" % liczba)
else:
    for index, value in enumerate(randomList):
        if(value == liczba):
            print("Element %i znajduje się na indeksie %i" % (liczba, index))
            break
#sprawdz ile razy dany elemtent wystepuje na liście

for liczba in randomList:
    if(value == liczba):
        count += 1
print("Element %i występuję w liście %i razy" % (value, count))