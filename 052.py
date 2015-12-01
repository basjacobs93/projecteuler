import time, math, helpers, itertools

start = time.clock()

for i in itertools.count(1):
  for j in range(2, 7):
    if not helpers.is_permutation(i, i*j):
      break
    if j==6:
      print i
      print time.clock()-start
      quit()