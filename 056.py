import time, math, helpers
start = time.clock()

maxsum = 0

for a in range(1, 100):
  for b in range(1, 100):
    q = helpers.digitsum(a**b)
    if q > maxsum:
      maxsum = q
      
print maxsum

print time.clock() - start