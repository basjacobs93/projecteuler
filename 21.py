import math

def d(n):
    sum = 1
    for i in range(2,math.floor(math.sqrt(n))):
        if n%i == 0:
            sum += i + n//i
    return sum

def amicable(n):
    a = d(n)
    return a != n and n == d(a)

sum = 0
for n in range(1,10001):
    if amicable(n):
        sum += n
        print(n)
print(str(sum))
