import math

def nthprime(n):
    counter = 1
    primelist = [2]
    i=3
    while True:
        prime = True
        for j in primelist:
            if j > math.sqrt(i):
                break
            if i%j == 0:
                prime = False
                break
        if prime == True:
            primelist.append(i)
            counter += 1
        if counter == n:
            return i
        i += 2


print(str(nthprime(10001)))
