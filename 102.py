#!/usr/bin/python

def contains0(a1,a2,b1,b2,c1,c2):
	return intersect(a1,a2,b1,b2,c1,c2) and intersect(b1,b2,c1,c2,a1,a2) and intersect(c1,c2,a1,a2,b1,b2)

def intersect(a1, a2, b1, b2, c1, c2):
	#calculate the point of intersection of A0 and BC
	d=a1*(b2-c2)-a2*(b1-c1)
	if d==0:
		return False
	else:
		d+=.0
		px=a1*(b1*c2-b2*c1)/d
		py=a2*(b1*c2-b2*c1)/d
		if ((px==0 and a1==0) or px/abs(px)==a1/abs(a1)) and ((py==0 and a2==0) or py/abs(py)==a2/abs(a2)):
			if px==0 and a1==0 and py==0 and a2==0:
				return False
			else:
				return True
		else:
			return False

tot=0
with open("102_triangles.txt") as f:
	for line in f:
		a1,a2,b1,b2,c1,c2 = [int(i) for i in line.split(",")]
		if contains0(a1,a2,b1,b2,c1,c2):
			tot+=1
			
print tot