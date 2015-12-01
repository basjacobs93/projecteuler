import math, time, itertools, helpers, re

start = time.clock()

def greater(card1, card2): #1: card1 is greater, 0: same, -1: card2 is greater
  if card1[:-1] == card2[:-1]:
    return 0
  for i in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
    if card1[:-1] == i:
      return -1
    if card2[:-1] == i:
      return 1

def high_card(hand):
  greatest = "2D"
  for i in hand:
    if greater(i, greatest) >= 0:
      greatest = i
  return greatest

def one_pair(hand):
  greatest = "2Q"
  for i in hand:
    for j in hand:
      if i!=j and greater(i, j)==0 and greater(i, greatest)>=0:
        greatest = i
  if greatest == "2Q":
    return 0
  else:
    return greatest

def two_pairs(hand):
  hand1 = list(hand)
  a = one_pair(hand)
  if a != 0:
    hand1.remove(a)
    b = one_pair(hand1)
    if b != 0:
      return (a, b)
  return 0
  
def three_of_a_kind(hand):
  hand1 = list(hand)
  a = one_pair(hand)
  if a != 0:
    hand1.remove(a)
    b = one_pair(hand1)
    if b != 0 and greater(a, b) == 0:
      return a
  return 0
  
def straight(hand):
  tot = 0
  for i in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
    found = False
    for j in hand:
      if j[:-1] == i:
        found = True
        break
    if found:
      tot += 1
      if tot == 5:
        return high_card(hand)
    else:
      tot = 0
  return 0
  
def flush(hand):
  color = hand[0][-1:]
  for i in hand:
    if i[-1:] != color:
      return 0
  return high_card(hand)
  
def full_house(hand):
  a = two_pairs(hand)
  hand1 = list(hand)
  hand2 = list(hand)
  if a != 0:
    hand1.remove(a[0])
    hand2.remove(a[1])
    if two_pairs(hand1):
      return two_pairs(hand1)
    if two_pairs(hand2):
      return two_pairs(hand2)
  return 0
    
def four_of_a_kind(hand):
  a = three_of_a_kind(hand)
  hand1 = list(hand)
  if a != 0:
    hand1.remove(a)
    if three_of_a_kind(hand1):
      return a
  return 0
  
def straight_flush(hand):
  if flush(hand) != 0 and straight(hand) != 0:
    return straight(hand)
  return 0
    
def royal_flush(hand):
  if flush(hand) != 0 and straight(hand) != 0 and straight(hand)[0] == "A":
    return straight(hand)
  return 0
  
def winner(hand1, hand2):
  if royal_flush(hand1):
    return 1
  if royal_flush(hand2):
    return 2
  if straight_flush(hand1):
    if straight_flush(hand2):
      if greater(straight_flush(hand1), straight_flush(hand2)) == 1:
        return 1
      else:
        return 2
    else:
      return 1
  if straight_flush(hand2):
    return 2
  if four_of_a_kind(hand1):
    if four_of_a_kind(hand2):
      if greater(four_of_a_kind(hand1), four_of_a_kind(hand2)) == 1:
        return 1
      elif greater(four_of_a_kind(hand1), four_of_a_kind(hand2)) == -1:
        return 2
      elif greater(high_card(hand1), high_card(hand2)) == 1:
        return 1
      else:
        return 2
    else:
      return 1
  if four_of_a_kind(hand2):
    return 2
  if full_house(hand1):
    if full_house(hand2):
      if greater(full_house(hand1), full_house(hand2)) == 1:
        return 1
      else:
        return 2
    else:
      return 1
  if full_house(hand2):
    return 2
  if flush(hand1):
    if flush(hand2):
      if greater(flush(hand1), flush(hand2)) == 1:
        return 1
      else:
        return 2
    else:
      return 1
  if flush(hand2):
    return 2
  if straight(hand1):
    if straight(hand2):
      if greater(flush(hand1), flush(hand2)) == 1:
        return 1
      else:
        return 2
    else:
      return 1
  if straight(hand2):
    return 2
  if three_of_a_kind(hand1):
    if three_of_a_kind(hand2):
      if greater(three_of_a_kind(hand1), three_of_a_kind(hand2)) == 1:
        return 1
      elif greater(three_of_a_kind(hand1), three_of_a_kind(hand2)) == -1:
        return 2
      elif greater(high_card(hand1), high_card(hand2)) == 1:
        return 1
      else:
        return 0
    else:
      return 1
  if three_of_a_kind(hand2):
    return 2


tot = 0
f = open("/Users/Bas/Desktop/p054_poker.txt", "r")
for line in f:
  splt = line.split()
  pl1 = splt[:5]
  pl2 = splt[-5:]
  if winner(pl1, pl2) == 1:
    tot += 1

print tot
print time.clock()-start