#n_silnia
# n! = n(n-1)(n-2)
# 5! = 5*4*3*2*1

def strong(n):
    result = 1
    while(n > 1):
        result *= n # result = result * n
        n -= 1
    return result

n=10
print("%d!=%d, %d" %(n, strong(n), len(str(strong(n)))))

def strongRec(n):
    if(n == 2):
        return n
    return n * strongRec(n - 1)
n=10
print(strongRec(n))