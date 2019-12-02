# tabliczka mnożenia 10x10
x = range(1,11)
for k in x:
    for v in x:
        print("%3i" % (k*v), end=" ")
    print()

y = range(3,10)
for k in y:
    print("%i ^ 2 = %i" % (k, k ** 2))