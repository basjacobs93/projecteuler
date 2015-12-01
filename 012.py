import math

def factorcount(n):
    a = 0
    for i in range(1, math.floor(math.sqrt(n+1))):
        if n%i == 0:
            a = a+2
    return a
for n in range(10000,20000):
    a = n*(n+1)//2
    b = factorcount(a)
    if b>500:
        print(str(a) + ' heeft ' + str(b) + ' factoren')
        break
