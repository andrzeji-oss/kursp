# ykorzystując 3 arg sprawdz czy wprowadzona wartośc z klawiatury jest liczbą
# jeżeli tak, to wypisz tę liczbę
# jeżeli nie, to wypisz zero

toNumber = input("podaj liczbę  ")
number = int(toNumber) if toNumber.isdecimal() else 0
print("Wynik działania ", number)