import time
import sympy
from sympy import factorint
from sympy import isprime
import math
T1 = time.time()
tijd = 0
def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer:
        return True
    else:
        return False

def find(n,a):
    max = int(n**.5) + 1
    for y in xrange(1, max + 2):
        d = n-a*y*y
        if d <= 0:
            return False
        if is_square(d):
            return True

def check2(n):
    a1, a2, a3, a7 = find(n,1), find(n,2), find(n,3), find(n,7)
    if a1 and a2 and a3 and a7:
        return True
    else:
        print(n,a1,a2,a3,a7)
        return False

def check(n):
    test = float(n)
    if (test/2).is_integer() and not (test/4).is_integer():
        return False
    T1 = time.time()
    primes = sympy.factorint(n)
    global tijd
    tijd += time.time()-T1
    count1 = 0
    count2 = 0
    count3 = 0
    count7 = 0
    for p in primes:
        power = primes[p] % 2
        if p % 4 == 3:
            if power == 1:
                return False
            count1 += 1
        else:
            if p != 2:
                count1 -= 10000
            count1 += 1

        if p % 8 in {5, 7}:
            if power == 1:
                return False
            count2 += 1
        else:
            if p != 2:
                count2 -= 10000
            count2 += 1

        if p % 3 == 2:
            if power == 1:
                return False
            if p == 2:
                count3 -= 10000
            count3 += 1
        else:
            if p != 3:
                count3 -= 10000

        if p % 7 in {3, 5, 6}:
            if power == 1:
                return False
            count7 += 1
        else:
            if p != 7 and p != 2:
                count7 -= 10000
            if p == 2:
                if primes[p] > 2:
                    count7 -= 10000
    if count1 > 0 or count2 > 0 or count3 > 0 or count7 > 0:
        return False
    return True

def check_prime(p):
    if p % 3 == 2:
        return False
    if p % 8 in {3, 5, 7}:
        return False
    if p % 7 in {3, 5, 6}:
        return False
    return True

def squares(limit=10**7):
    set1, set2, set3, set7 = set(), set(), set(), set()
    max = int(limit**.5) + 1
    for a in xrange(1, max):
        a2 = a*a
        if a % 10**4 == 0:
            print(a)
        for b in xrange(1, max):
            b2 = b*b
            d = a2 + b2
            if d > limit:
                break
            if d % 16 in {0, 1, 4, 9}:
                set1.add(d)
            d += b2
            if d > limit:
                continue
            if d % 16 in {0, 1, 4, 9}:
                set2.add(d)
            d += b2
            if d > limit:
                continue
            if d % 16 in {0, 1, 4, 9}:
                set3.add(d)
            d += 4*b2
            if d > limit:
                continue
            if d % 16 in {0, 1, 4, 9}:
                set7.add(d)
    finalset = set1 & set2 & set3 & set7
    return finalset

def findSquares(limit = 10**5, primes = set()):
    tot = 0
    for n in xrange(5, limit + 1):
        if n in primes:
            for i in xrange(1, limit):
                new = n*i*i
                if new > limit:
                    break
                tot += 1
        n2 = n*n
        if n2 > limit:
            continue
        if check(n2):
            for i in xrange(1, limit):
                new = n2*i*i
                if new > limit:
                    break
                tot += 1
    return tot

def singlePrimes(limit=2*10**9):
    print("All numbers <", limit, ":")
    TSingle = time.time()
    primes = set()
    for x in xrange(1, int(limit**.5) + 1, 2):
        x2 = x**2
        for y in xrange(4, limit, 4):
            quad = x2 + 7*y*y
            if quad > limit:
                break
            if quad % 168 in {1, 25, 121}:
                if isprime(quad):
                    primes.add(quad)
    print("Single primes:", len(primes), "in", time.time() - TSingle,"seconds")
    return primes

def doublePrimes(primes = set(), limit=2*10**9):
    TDouble = time.time()
    double_primes= set()
    primes = sorted(primes)
    max = int(limit**.5) + 1
    for p1 in primes:
        for p2 in primes:
            if p2 < p1:
                if p1*p2 < limit:
                    double_primes.add(p1*p2)
                else:
                    break
            else:
                break
    print("Double primes:",len(double_primes), "in", time.time() - TDouble,"seconds")
    return double_primes

def triplePrimes(singleprimes = set(), doubleprimes = set(), limit=2*10**9):
    TTriple = time.time()
    tripleprimes = set()
    for p1 in singleprimes:
        if p1 < 40000:
            for p2 in doubleprimes:
                if p1*p2 < limit:
                    tripleprimes.add(p1*p2)
    print("Triple primes:", len(tripleprimes), "in", time.time() - TTriple,"seconds")
    return tripleprimes

def allPrimes(limit=2*10**9):
    singleprimes = singlePrimes(limit)
    doubleprimes = doublePrimes(singleprimes,limit)
    allprimes = singleprimes | doubleprimes | triplePrimes(singleprimes, doubleprimes,limit)
    print("All primes:",len(allprimes))
    return allprimes


T1 = time.time()
limit = 2*10**9
primes = allPrimes(limit)
solution = findSquares(limit,primes)
print("result:", solution)
T2 = time.time()
print(T2-T1)
