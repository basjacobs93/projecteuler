#!/usr/bin/python

import helpers, time, itertools

start = time.clock()

def triangle(n):
	return str(n*(n+1)/2)
	
def square(n):
	return str(n*n)
	
def pentagonal(n):
	return str(n*(3*n-1)/2)
	
def hexagonal(n):
	return str(n*(2*n-1))
	
def heptagonal(n):
	return str(n*(5*n-3)/2)
	
def octagonal(n):
	return str(n*(3*n-2))

def findset(first, second, third, fourth, fifth, sixth):
	for n in range(200):
		frst = first(n)
		if len(frst)>3:
			if len(frst)>4:
				break
			for o in range(200):
				scnd = second(o)
				if len(scnd)>3:
					if len(scnd)>4:
						break
					if frst[-2:] == scnd[:2]:
						for p in range(200):
							thrd = third(p)
							if len(thrd)>3:
								if len(thrd)>4:
									break
								if scnd[-2:] == thrd[:2]:
									for q in range(200):
										frth = fourth(q)
										if len(frth)>3:
											if len(frth)>4:
												break
											if thrd[-2:] == frth[:2]:
												for r in range(200):
													ffth = fifth(r)
													if len(ffth)>3:
														if len(ffth)>4:
															break
														if frth[-2:] == ffth[:2]:
															for s in range(200):
																sxth = sixth(s)
																if len(sxth)>3:
																	if len(sxth)>4:
																		break
																	if ffth[-2:] == sxth[:2] and sxth[-2:] == frst[:2]:
																		print "{0} + {1} + {2} + {3} + {4} + {5} = {6}".format(frst, scnd, thrd, frth, ffth, sxth, int(frst)+int(scnd)+int(thrd)+int(frth)+int(ffth)+int(sxth))

for i in itertools.permutations((square, pentagonal, hexagonal, heptagonal, octagonal)):
	findset(triangle, i[0], i[1], i[2], i[3], i[4])			

print time.clock()-start