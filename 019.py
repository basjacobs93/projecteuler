import math

def is_leapyear(year):
  if (year%4 == 0 and year%100 != 0) or year%400 == 0:
    return True
  return False

count = 0

months = [31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30] #dec, jan, feb, ..., nov
  
firstday = 6

for year in range(1901, 2001):
  if is_leapyear(year):
    months[2] = 29
  else:
    months[2] = 28
  for month in range(1, 13):
    firstday = (firstday + months[month-1] - 1)%7 + 1
    if firstday == 7:
      print year, month
      count += 1
print count, 'sundays'