tupleType = (1,2,3,4,5)
# tupleType[1] = 55 krotka jest typem niezmiennym

multiDimTuple = ([1,2], [3,4], [5,6])
# multiDimTuple[0] = 1 wywali błąd

multiDimTuple[0].append('x')
print(multiDimTuple)
