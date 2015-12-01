import numpy as np

maxnumer = 2
maxdec = 0

for numer in range(2,1000):
  maxdecim = 0
  if numer%2 != 0 and numer%5 != 0:
    for i in range(1, 2000):
      if (10**i-1)%numer == 0:
        maxdecim = i
        if maxdecim > maxdec:
          maxdec = maxdecim
          maxnumer = numer
        break
    
print maxnumer, maxdec