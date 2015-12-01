import math

def digitfactorial(n):
  tot = 0
  while n>0:
    tot += factlist[n%10]
    n = n//10
  return tot

factlist = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

tot = 0

for n in range(10, 362880*9):
  if n == digitfactorial(n):
    print n
    tot += n
    
print 'tot', tot