def bubbleSort(elements, asc=False):
    #pętla iterująca po kolejnych próbach sortowania
    noProbes = 1
    for probe in range(len(elements)-1):          #determinujemy 5 prob w przypadku najgorszym
        isSorted = True
        for index, value in enumerate(elements):
            if(index == len(elements) - 1):
                break
            if(elements[index] > elements[index + 1] and asc):      #porownanie sąsiednich komórek
                isSorted = False
                elem = elements[index + 1]          #wydobycie elementu na indeksie i+1 do zmiennej
                elements[index + 1] = elements[index]
                elements[index] = elem
            if (elements[index] < elements[index + 1] and not asc):  # porownanie sąsiednich komórek
                isSorted = False
                elem = elements[index + 1]  # wydobycie elementu na indeksie i+1 do zmiennej
                elements[index + 1] = elements[index]
                elements[index] = elem
        print(noProbes, elements)
        if(isSorted):
            break
        noProbes += 1
    return elements
from datetime import datetime

t_start = datetime.now().microsecond
print(bubbleSort([8,24,343,1,323,4,5, 56,5,6,37,38,212,32,56,65,3,4,4,5,2,3,4,343,]))
t_stop = datetime.now().microsecond

print(t_start)
print(t_stop)
print("Czas wyloania funkcji", (t_stop-t_start))
