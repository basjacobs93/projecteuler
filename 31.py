import itertools, time

start = time.clock()

coins = [1, 2, 5, 10, 20, 50, 100, 200]

def number(n, coins):
  totsum = 0  #aantal mogelijkheden
  if n==0:  #je bent klaar
    return 1
  elif len(coins) == 0:
    return 0
  elif n >= coins[-1]: #de laatste coin past
    for i in range(201):  #kijk hoe vaak hij past
      if n < i*coins[-1]:
        break
      else:
        totsum += number(n-i*coins[-1], coins[:-1])
  else:
    totsum += number(n, coins[:-1])
  return totsum

print number(200, coins)
print time.clock()-start