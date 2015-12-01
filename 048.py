import math, time

start = time.clock()

sum = 0

for i in range(1, 1000+1):
  sum += i**i

print sum%10**10

print time.clock()-start