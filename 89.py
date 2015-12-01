#!/usr/bin/python

rom_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

int_to_rom = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}

TABLE=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]

def to_int(s):
	tot = 0
	last = 0
	updown = 1
	for i in s[::-1]:
		a = rom_to_int[i]
		if a<last:
			updown = -1
		elif a>last:
			updown = 1
		last = a
		tot += updown*a
	return tot

def to_rom (n):
	parts = []
	for letter, value in TABLE:
		while value <= n:
			n -= value
			parts.append(letter)
	return ''.join(parts)

sum = 0

with open("/Users/Bas/Desktop/p089_roman.txt") as f:
	for line in f:
		a = len(line.strip())
		b = len(to_rom(to_int(line.strip())))
		if b<a:
			sum += a-b
print sum