import math

def ispalindrome(nmbr):
        if nmbr < 100000:
                if math.floor(nmbr/10000) == nmbr%10 and math.floor((nmbr%10000)/1000) == math.floor((nmbr%100)/10):
                        return True
        elif nmbr < 1000000:
                if math.floor(nmbr/100000) == nmbr%10 and math.floor((nmbr%100000)/10000) == math.floor((nmbr%100)/10) and math.floor((nmbr%10000)/1000) == math.floor((nmbr%1000)/100):
                        return True

lrgst = 0
#only checks numbers between 900 and 1000 since these are the biggest
for x in range(900, 1000):
        for y in range(900, 1000):
                if ispalindrome(x*y):
                        lrgst = x*y
print (str(lrgst))
