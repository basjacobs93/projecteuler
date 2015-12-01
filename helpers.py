import math

def is_prime(n):
  if n<2:
    return False
  if n%2 == 0:
    return False
  for i in range(3, int(math.sqrt(n))+1, 2):
    if n%i == 0:
      return False
  return True
  
def is_permutation(a, b):
  if sorted(str(a)) == sorted(str(b)):
    return True
  return False
  
def is_disjoint(a, b):
  for i in str(a):
    if i in str(b):
      return False
  return True

def is_pentagonal(n):
  x = (math.sqrt(24*n+1)+1)/6
  return int(x) == x

def is_hexagonal(n):
  x = (1+math.sqrt(1+8*n))/4
  return int(x) == x
  
def is_palindromic(n):
  strn = str(n)
  if len(strn) <= 1:
    return True
  if strn[0] == strn[-1]:
    return is_palindromic(strn[1:-1])
  else:
    return False
    
def digitsum(n):
  som = 0
  for i in str(n):
    som += int(i)
  return som