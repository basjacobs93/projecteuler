import math, time

start = time.clock()

def is_prime(n):
  for i in range(2, int(math.sqrt(n)+1)):
    if n%i==0:
      return False
  return True
  
def is_primecycle(n):
  if not is_prime(n):
    return False
  if n<10:
    return True
  strlen = len(str(n))
  string = str(n)*2
  for j in string:
    if int(j)%2==0 or int(j)%5==0:
      return False
  for i in range(strlen):
    if not is_prime(int(string[i:i+strlen])):
      return False
  return True

counter = 0

for n in range(2, 1000000):
  if is_primecycle(n):
    counter += 1
    print n
    
print 'count:', counter

end = time.clock()
print end-start