list = [1,2,3]
#czy dwa elementy listy są dodatnie
if(list[0] > 0 and list[1] > 0):
    print("dwa pierwsze elementy są doatnie")
elif(list[0] > 0 and list[1] <= 0):
    print("tylko 1 element jest dodatni")
else:
    print("Oba elementy są ujemne")

# sprawdz czy wprowadzona liczba jest parzysta

liczba = int(input("Wprowadź liczbę aby sprawdzić czy jest parzysta "))

print("Wprowadzona wartość jest: ", "parzysta" if (liczba % 2 == 0) else "nieparzysta")