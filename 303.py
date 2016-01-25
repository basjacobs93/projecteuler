'''
0    0,1,2,3,4,5,6,7,8,9
1    0,1,2        1,1,8
2    0,1,5,6      1,4,1,4
3    0,4,7        4,3,3
4    0,3,5,8      3,2,3,2
5    0,2,4,6,8    2,2,2,2,2
6    0,2,5,7      2,3,2,3
7    0,3,6        3,3,4
8    0,4,5,9      4,1,4,1
9    0,8,9        8,1,1


9 	    12222			        1358
99	    1122222222		        11335578
999	    111222222222222		    111333555778
9999	11112222222222222222	1111333355557778
'''

import time
T1 = time.time()

digits = [(1,1,1,1,1,1,1,1,1,1),(1,1,8),(1,4,1,4),(4,3,3),(3,2,3,2),(2,2,2,2,2),(2,3,2,3),(3,3,4),(4,1,4,1),(8,1,1)]


def check(n):
    for i in str(n):
        if int(i) > 2:
            return False
    return True

def f(n):
    if n%10==0:
        return 10*f(n/10)
    lst = digits[n%10]
    num = 0
    i = 0
    j = 0
    l = len(lst)
    while True:
        num += lst[j]*n
        i += 1
        if check(num):
            return num
        j = (j+1)%l

def finder(n, x):
    m = []
    for i in n:
        if i % x == 0:
            return i/x
        else:
            m.append(int(str(i)+'0'))
            m.append(int(str(i)+'1'))
            m.append(int(str(i)+'2'))
    n = m
    return finder(m,x)

def find(limit=10000):
    count = 0
    for n in xrange(1, limit-1):
        if n%999!=0:       
            fn = f(n)
            count += fn/n
            print n, fn
            
    #skipped some cases:
    count += 111333555778 #999
    count += 55666777889 #1998
    count += 37444851926 #2997
    count += 30335891447 #3996
    count += 222667111556 #4995
    count += 18722425963 #5994
    count += 17476222254 #6993
    count += 27680458236 #7992
    count += 13592728531 #8991
    count += 111333555778 #9990
    count += 1111333355557778 #9999
    count += 1 #10000

    return count

print find()

T2 = time.time()
print T2-T1