# utworz test korzystajacy z pojedynczej instrukcji if, ktory sprawdzi czy podana wartosc
# znajduje sie w przedziale odpowiadającym indeksom z listy [4,5,3,2,1,6]

lista = [4, 5, 3, 2, 1, 6]
value = int(input("którą wartość chcesz ustawić" + str(lista))) - 1

if (value >= 0 and value < len(lista)):
    print("Twój wybór:", lista[value])
else:
    print("Out of range")
