a = 2 + 5j
b = 4 + 6j

print(a + b)
print(4 - b)

print(bool(121), bool(0))
print(bool("blaaa"), bool(""))
print(bool((2,23,3)), bool( () ))

name = "andrzej"
print(len(name))
print(name[0])
print(name[len(name) -1])
print(name[-1])
# print(name[10]) tak ne mozna

name = name + " " + "nazwisko"
print(name)
print("add: " + name)
name = name[0:7]
print("sub: " + name)