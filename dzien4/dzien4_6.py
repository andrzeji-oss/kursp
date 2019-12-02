# napisz program obliczający odległość między dwoma punktami
from math import sqrt
def odleglosc(x1,y1,x2,y2):
    return sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))
x1 = 0
y1 = 0
x2 = 1
y2 = 1

print(odleglosc(x1,y1,x2,y2))

def odleglosc3d(x1,y1,z1,x2,y2,z2):
    return sqrt(pow(x1-x2, 2) + pow(y1-y2, 2) + pow(z1-z2, 2))

x1 = 1
y1 = 1
z1 = 1
x2 = 2
y2 = 2
z2 = 2

print(odleglosc3d(x1,y1,z1,x2,y2,z2))