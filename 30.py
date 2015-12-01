import math

def isfifthsum(n):
  sum = 0
  for i in range(int(math.log(n))):
    sum += (n//(10**i) % 10)**5
  return sum == n

total = 0

for i in range(2,1000000): #7*9^5 < 999.999, so the maximum number of digits is 6
  if isfifthsum(i):
    print i
    total += i
    
print 'sum:', total