import math

greatest = 0
number = 0

for n in range(1000000):
        a = n+1
        t = 1
        while a != 1:
                if a%2==0:
                        a = a/2
                else:
                        a = 3*a + 1
                t = t+1
        if t>greatest:
                greatest = t
                number = n+1
                print(str(number))
print(str(greatest)+" "+str(number))
