import math

primelist = [2]
i=3
sum = 2
while i<2000000:
    prime = True
    for j in primelist:
        if j > math.sqrt(i):
            break
        if i%j == 0:
            prime = False
            break
    if prime == True:
        primelist.append(i)
        sum += i
    i += 2

print(str(sum))
