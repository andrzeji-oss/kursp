# Napisz program OOP, ktory reprezentuje skladowe barw RGB
# R - red
# G - zielony
# B - niebieski
# Implementacja klasy modelu reprezentującej dowolny kolor [r,g,b]

class RGB:
    def __init__(self, r, g, b):
        if(r >= 0 and g >= 0 and b >=0 and r <= 255 and g <= 255 and b <= 255):
            self.r = r
            self.g = g
            self.b = b
        else:
            print("Podane wartości nie są poprawne")
            self = None

    def __add__(self, other):
        #utworzenie nowego obiektu na podstawie sumy składoweych rgb z dwóch kolorów
        c = RGB(self.r + other.r, self.g + other.g, self.b + other.b)
        return c

    def __eq__(self, other):
        return self.r == other.r and self.g == other.g and self.b == other.b

    def __str__(self):
        return "[%d, %d, %d]" % (self.r, self.g, self.b)

red = RGB(255,0,0)
green = RGB(0,255,0)
blue = RGB(0,0,255)
yellow = RGB(255,255,0)

mixed = red.__add__(green)
print(type(mixed))
print(red, green,blue,yellow, red.__add__(green), (red+green))

print("czy czerwony to zielony: ", red == green)
print("czy zolty to samo co czerwony + zielony: ", ("tak" if (yellow) == (red + green) else "nie"))

