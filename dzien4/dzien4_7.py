# zwroc sume i nty element ciagu geometrycznego, n=numer ciagu, a1 =

def geometricSeries(n, a1 = 1, q = 2):
    cumSum = 0
    elements = []
    for i in range (0, n - 1):
        cumSum += a1 * pow(q, i)
        elements.append(a1 * pow(q, i))
    return cumSum, elements

print(geometricSeries(10))

