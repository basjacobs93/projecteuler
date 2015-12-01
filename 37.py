import time

start = time.clock()

def is_prime(n):
  if n==1 or n==0:
    return False
  for i in range(2, int(n**0.5+1)):
    if n%i == 0:
      return False
  return True
  
def is_left_truncatable(n):
  if n<10:
    return is_prime(n)
  elif is_prime(n):
    return is_left_truncatable(int(str(n)[1:]))
  else:
    return False

def is_right_truncatable(n):
  if n<10:
    return is_prime(n)
  elif is_prime(n):
    return is_right_truncatable(int(str(n)[:-1]))
  else:
    return False
    
sum = 0
number = 0

for i in range(11, 1000000, 2):
  if number == 11:
    break
  if is_right_truncatable(i) and is_left_truncatable(i):
    print i
    sum += i
    number += 1

print 'sum', sum

print time.clock()-start