print(str(round((5500/168),2)) + " netto za godzine \n" + str(round((5500/168*1.23),2)) + " brutto za godzine")

p = False
q = False
print(not(p and q) == ((not p) or (not q)))

p = False
q = True
print(not(p and q) == ((not p) or (not q)))

p = True
q = False
print(not(p and q) == ((not p) or (not q)))

p = True
q = True
print(not(p and q) == ((not p) or (not q)))

