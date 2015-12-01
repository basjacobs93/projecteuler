import time

start = time.clock()

def number_of_solutions(perim):
  num = 0
  for r in range(1, perim/2):
    for s in range(1, r+1):
      if r*(1+s) == perim:
        num += 1
  return num

maxn = 0

for p in range(2, 1001, 2):
  solnum = number_of_solutions(p)
  if solnum > maxn:
    maxn = solnum
    maxp = p

print maxp

print time.clock()-start