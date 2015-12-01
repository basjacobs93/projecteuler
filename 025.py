import math

lijst = [1,1]

n=2
while True:
    sum = lijst[n-1] + lijst[n-2]
    lijst.append(sum)
    if sum>=10**999:
        print(str(sum) + " " + str(n+1))
        break
    else:
        n += 1
