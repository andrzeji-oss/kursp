# inicjalizacja wartości globalnej w skrypcie

globalID = 0
class Player:
    def __init__(self, name, lastname, repr, weight, height):
        self.name = name
        self.lastname = lastname
        self.repr = repr
        self.weight = weight
        self.height = height
        global globalID     #modyfikacja wartości globalnej w skrypcie
        globalID += 1       # global -> wskażnik globalny niezwiązany z klasą player
        self.id = globalID  # self -> id dla konkretnego obiektu
    def calculateBMI(self):
        return self.weight/pow(self.height/100,2)
    def __str__(self):
        global globalID     #odczyt wartości globalnej w skrypcie
        return ("| %3d |%10s | %10s | %10s | %10d | %10d | %f10.2"
                % (self.id,
                   self.name,
                   self.lastname,
                   self.repr,
                   self.weight,
                   self.height,
                   self.calculateBMI()))

p1 = Player("Adam", "Małysz", "Pol", 50, 165)
p2 = Player("Kamil", "Stoch", "Pol", 75, 183)
p3 = Player("Jan", "rus", "Pol", 70, 150)
p4 = Player("tata", "srata", "Pol", 45, 167)

print(p1)
print(p2)
print(p3)
print(p4)

players = [p1,p2,p3,p4]
def getPlayers():
    for player in players:
        print(player)

def findPlayerById(findId):
    for player in players:
        if(player.id == findId):
            print(player)
print()
findPlayerById(1)
