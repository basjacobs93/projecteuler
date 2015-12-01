import math
lrgst = 0
number = 600851475143
divisor = 2
while divisor < math.sqrt(600851475143):
        if number/divisor%1==0:
                lrgst = divisor
                number = number/divisor
                divisor = 2
                print (lrgst)
        else:
                divisor = divisor + 1
print ('done')
