import math, time
from fractions import Fraction

start = time.clock()

counter = 0

frac = Fraction(3/2)
for i in range(999):
  if len(str(frac.denominator)) < len(str(frac.numerator)):
    counter += 1
  frac = 1+1/(1+frac)

print counter

print time.clock()-start