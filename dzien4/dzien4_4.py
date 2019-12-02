# funkcja zwracajaca wartosc zadanego ciagu Fibonacciego i obliczajacy sumę elementów ciągu

def fibonacci(n):
    if(n == 0):
        return  []
    if(n == 1):
        return [0]
    fibo = [0,1]
    cumSum = 1
    for i in range(2,n):
        fibo.append(fibo[i-1] + fibo[i-2])
        cumSum += fibo[i]
    return fibo, fibo[len(fibo)-1], cumSum


n = 5
print(fibonacci(n))
print("Wygląd ciągu: %s\nn-ty element: %d \nsuma: %d"  % fibonacci(n) )