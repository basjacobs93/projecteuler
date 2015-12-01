import time

start = time.clock()

row = ''
for i in range(10**6+1):
  row += str(i)

prod = 1
for j in range(7):
  print row[10**j]
  prod *= int(row[10**j])
  
print prod

print time.clock()-start