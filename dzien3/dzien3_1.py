# sklep internetowy

# dane: slownik ID -> lista cech
products = { "1": ["A",3.5,10],
             "2": ["B",2.99,5],
             "3": ["C", 9.99,1]}

# koszyk zawiera listy zamówionych produktów
basket = []
cumSum = 0

#CLI użytkownika
while(True):
    #pętla wypisująca produkty
    print("| %3s | %10s | %10s | %5s |" % ("ID", "NAZWA", "CENA", "ILOŚć"))
    for key in products.keys():
        print("| %3s | %10s | %8.2fzł | %5.1f |" % (key, products[key][0], products[key][1], products[key][2]))

    choice = input("\nCo chcesz zamówić, podaj ID produktu lub q - wyjście  \n")
    if(choice.lower() == "q"):
        print("Wyjście")
        break

    # sprawdzenie czy taki produkt istnieje
    if(choice not in products.keys()):
        print("Nie ma takiego produktu")
        continue

    # prosimy o wprowadzenie ilości
    while(True):
        try:
            quantity = float(input("Wprowadź ilość zamawianego produktu  "))
        except:
           print("Błędny typ danych. Wprowadź liczbę!!!!!")
           continue
        if (quantity > products[choice][2] and quantity >= 0):
            print("Dostępnych jest tylko: " + str(products[choice][2]) + "szt.")
            continue
        else:
            break


    #aktualizacja magazynu i koszyka
    products[choice][2] -= quantity
    basket.append([products[choice][0], products[choice][1], products[choice][2]])

    #suma skumulowana zamówienia
    cumSum += quantity *products[choice][1]
    print("Twój koszyk: ")
    for element in basket:
        print("| %10s | %8.2fzł | %5.1f |" % (element[0].center(10), element[1], element[2]))
    print("\nSuma do zapłaty: %.2f zł" % cumSum + "\n")
