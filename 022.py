import sys
file = open('/Users/Bas/Desktop/p022_names.txt', 'rU')
names = ['',]
for name in file.read().split(','):
  names.append(name[1:-1].strip())
names.sort()


total = 0
for i in range(1,len(names)):
  subtotal = 0
  for letter in names[i]:
    subtotal += ord(letter)-64
  #print i, names[i], subtotal, subtotal*i
  total += subtotal*i
  
print total