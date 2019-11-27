spk = float(input("Podaj wkład: "))
p = int(input("Podaj oprocentowanie: "))/100
n = int(input("Podaj liczbę lat: "))
m = int(input("Podaj częstotliwość kapitalizaji: "))

#print("Twoje oszczędności: " + str(spk(1+float(p/k/100))**(n*k))) to zle
print("Twoje oszczędności: " + str(round(spk * (1 + (p/m)) ** (n * m),2)))
