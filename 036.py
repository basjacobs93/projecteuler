import time

start = time.clock()

def is_palindromic(n):
  strn = str(n)
  if len(strn) <= 1:
    return True
  if strn[0] == strn[-1]:
    return is_palindromic(strn[1:-1])
  else:
    return False

sum = 0

for i in range(1, 1000000, 2):
  if is_palindromic(i) and is_palindromic(bin(i)[2:]):
    print i
    sum += i
    
print 'sum', sum
end = time.clock()
print end-start