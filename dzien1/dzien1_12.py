a = False
b = False
c = True

print(((not a) and (not b) and (not c)) or ((not a) and (not b) and c) or ((not a) and b and (not c)) or (a and (not b) and (not c)))

