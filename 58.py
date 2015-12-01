import time, math, helpers

start = time.clock()

primecount = 0
totcount = 1

num = 1
for i in range(2, 100000, 2):
  for j in range(4):
    if helpers.is_prime(num):
      primecount += 1
    totcount += 1
    num += i
  if float(primecount)/float(totcount)<0.10:
    print i+1
    print time.clock()-start
    quit()