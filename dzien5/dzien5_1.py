class Warcaby:
    #pole klasowe -> słownik zawierający 8 słowników
    warcaby = {
        8: {1: " ", 2: "O", 3: " ", 4: "O", 5: " ", 6: "O", 7: " ", 8: "O"},
        7: {1: "O", 2: " ", 3: "O", 4: " ", 5: "O", 6: " ", 7: "O", 8: " "},
        6: {1: " ", 2: "O", 3: " ", 4: "O", 5: " ", 6: "O", 7: " ", 8: "O"},
        5: {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " "},
        4: {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " "},
        3: {1: "X", 2: " ", 3: "X", 4: " ", 5: "X", 6: " ", 7: "X", 8: " "},
        2: {1: " ", 2: "X", 3: " ", 4: "X", 5: " ", 6: "X", 7: " ", 8: "X"},
        1: {1: "X", 2: " ", 3: "X", 4: " ", 5: "X", 6: " ", 7: "X", 8: " "}
    }

    #metoda klasowa wypisująca szachownicę
    def printBoard(self):
        # iteracja po sekwencji wierszy
        print(" | %1s | %1s | %1s | %1s | %1s | %1s | %1s | %1s |" % ("A", "B", "C", "D", "E", "F", "G", "H"))
        for row in self.warcaby.keys():
            #iteracja po polach w wierszu
            print("%1d" % (row), end="")
            for key in self.warcaby[row].keys():
                print("|%2s " % (self.warcaby[row][key]), end = "")
            print("| %1d \n" % (row),end="")
        print(" | %1s | %1s | %1s | %1s | %1s | %1s | %1s | %1s |" % (
        "A", "B", "C", "D", "E", "F", "G", "H"))
        print()

    def getPoint(self):
        print(self.warcaby[3][3])
    def returnMovesForPoint(self, rowStart, columnStart, rowStop, columnStop, type):
        # sprawdzam czy punkty znajduj sie w kluczach naszych slownikow
        if(rowStart in self.warcaby.keys() and columnStart in self.warcaby[rowStart].keys()):
            # sprawdzanie poprawnosci ruchu pionka "X"
            if(type == "X" and (rowStop == (rowStart + 1)
                                and (columnStop == (columnStart + 1)) or (columnStop == (columnStart - 1))
            and columnStop >= 1 and columnStop <= 8 and rowStop >= 1 and rowStop <= 8)):
                print("ruch poprawny dla pionka X")
                self.movePoint(rowStart, columnStart, rowStop, columnStop, type)
            # sprawdzenie poprawnoci ruch dla pionka "O"
            elif (type == "O" and (rowStop == (rowStart - 1) and (columnStop == (columnStart + 1)) or (
                        columnStop == (columnStart - 1)) and columnStop >= 1 and columnStop <= 8 and rowStop >= 1 and rowStop <= 8)):
                self.movePoint(rowStart, columnStart, rowStop, columnStop, type)
                print("ruch poprawny dla pionka O")
            else:
                print("bledny ruch")
        else:
            print("bledny adres pionka")

    def movePoint(self,rowStart, columnStart, rowStop, columnStop, type):
        #przesuniecie pionka na now pozycje
        self.warcaby[rowStop][columnStop] = type
        #aktualizacja pustego miejsca pozostaego po pionku
        self.warcaby[rowStart][columnStart] = "  "
        self.printBoard()

w1 = Warcaby()
w1.printBoard()

w1.getPoint()
#w1.returnMovesForPoint(6,2,5,3,"O")
w1.movePoint(6,2,5,3,"O")
w1.movePoint(3,1,4,2,"X")
