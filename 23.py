import math

def divisorsum(n):
  sum = 1
  for i in range(2, int(math.sqrt(n))+1):
    if n%i == 0:
      if i*i == n:
        sum += i
      else:
        sum += i + n//i
  return sum

def isabundant(n):
  return divisorsum(n) > n

abundantlist = [x for x in range(1,20162 + 1) if isabundant(x)] #list with abundant numbers
    
print len(abundantlist)

def abundantsum(n):
  for i in abundantlist:
    if i > n:
      return False
    if (n-i) in abundantlist:
      return True
  return False
  
print sum(x for x in range(1, 20162 + 1) if not abundantsum(x))