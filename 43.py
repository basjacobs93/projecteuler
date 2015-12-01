import time, itertools

start = time.clock()

def isdiv(number):
  if int(number[7:10])%17 != 0:
    return False
  if int(number[6:9])%13 != 0:
    return False
  if int(number[5:8])%11 != 0:
    return False
  if int(number[4:7])%7 != 0:
    return False
  if int(number[5])%5 != 0:
    return False
  if int(number[2:5])%3 != 0:
    return False
  if int(number[3])%2 != 0:
    return False
  return True

sumnum = 0

for num in itertools.permutations('0123456789'):
  number = ''.join(map(str, num))
  if int(number)%2!=0:
    if isdiv(number):
      print number
      sumnum += int(number)

print 'sum', sumnum

print time.clock() - start