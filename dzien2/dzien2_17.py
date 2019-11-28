# wprowadz dane z klawiatury do listy tak dlugo az uzytkownik wpisze q
elements = []
while(True):
    elem = input("podaj wartość lub wprowadź q żeby wyjść   ")
    if(elem.lower() == "q"):
        print("wyjście")
        break
    elements.append(elem)
print(elements)

