#!/usr/bin/python

counter = 0
tot = 0

def check(sudoku,opts): # check if sudoku is valid
	for i in range(9):
		for j in range(9):
			if sudoku[i][j]==0 and opts[i][j]==[]:
				return False
	for i in range(9): # check rows
		row = []
		for j in range(9):
			if sudoku[i][j]!=0:
				if sudoku[i][j] in row:
					return False
				else:
					row.append(sudoku[i][j])
	for j in range(9): # check columns
		col = []
		for i in range(9):
			if sudoku[i][j]!=0:
				if sudoku[i][j] in col:
					return False
				else:
					col.append(sudoku[i][j])
	for i in range(3): # check blocks
		for j in range(3):
			block = []
			for k in range(i*3, i*3+3):  
				for l in range(j*3, j*3+3):
					if sudoku[k][l]!=0:
						if sudoku[k][l] in block:
							return False
						else:
							block.append(sudoku[k][l])
	return True

def done(sudoku): # check if sudoku is filled out entirely
	for i in range(9):
		for j in range(9):
			if sudoku[i][j]==0:
				return False
	return True

def crossout(opts, i, j, elem): # crosses out options if one is filled in
	for k in range(9):	# cross out in rows and columns
		if elem in opts[i][k]:
			opts[i][k].remove(elem)
		if elem in opts[k][j]:
			opts[k][j].remove(elem)
	for k in range(i/3*3, i/3*3+3):  # cross out in 3x3 blocks
		for l in range(j/3*3, j/3*3+3):
			if elem in opts[k][l]:
				opts[k][l].remove(elem)
	return opts

def sweep(sudoku, opts): # sweeps rows and columns until no longer possible
	found = True
	while found and not done(sudoku):
		found = False
		for i in range(9):
			for j in range(9):
				if len(opts[i][j]) == 1: # only one possibility
					sudoku[i][j] = opts[i][j][0] # fill it in
					opts[i][j] = []
					opts = crossout(opts, i, j, sudoku[i][j])
					found = True
	
	return sudoku, opts
	
def uniques(sudoku, opts): #finds unique elements in a row and column
	# row
	for i in range(9):
		multip = [0 for _ in range(10)] # counter
		for j in range(9):
			for k in opts[i][j]:
				multip[k] += 1
		for k in range(1,10):
			if multip[k] == 1: # element occurs only once
				for j in range(9):
					if k in opts[i][j]:
						sudoku[i][j]=k
						opts[i][j]=[]
						opts = crossout(opts, i, j, k)
	# column
	for i in range(9):
		multip = [0 for _ in range(10)] # counter
		for j in range(9):
			for k in opts[j][i]:
				multip[k] += 1
		for k in range(1,10):
			if multip[k] == 1: # element occurs only once
				for j in range(9):
					if k in opts[j][i]:
						sudoku[j][i]=k
						opts[j][i]=[]
						opts = crossout(opts, j, i, k)
	# block
	for i in range(3):
		for j in range(3):
			multip = [0 for _ in range(10)]
			for k in range(3*i,3*i+3):
				for l in range(3*j,3*j+3):
					for m in opts[k][l]:
						multip[m] += 1
			for k in range(1,10):
				if multip[k] == 1:
					for l in range(3*i,3*i+3):
						for m in range(3*j,3*j+3):
							if k in opts[l][m]:
								sudoku[l][m]=k
								opts[l][m]=[]
								opts = crossout(opts,l,m,k)
	return sudoku, opts
	
def twins(sudoku, opts):
	for row in opts: # look for twins in a row
		pairs = []
		foundpair = False
		for i in row:
			if len(i)==2:
				if i in pairs:
					# we found twins!
					foundpair = i
					break
				else:
					pairs.append(i)
		if foundpair: # cross out twins
			for i in row:
				if i!=foundpair:
					for k in foundpair:
						if k in i:
							i.remove(k)
							
	sudoku, opts = sweep(sudoku, opts) # sweep everything
	sudoku, opts = uniques(sudoku, opts)

	for i in range(9): # look for twins in column
		pairs = []
		foundpair = False
		for j in range(9):
			if len(opts[j][i])==2:
				if opts[j][i] in pairs:
					foundpair = opts[j][i]
					break
				else:
					pairs.append(opts[j][i])
		if foundpair:
			for j in range(9):
				if opts[j][i]!=foundpair:
					for k in foundpair:
						if k in opts[j][i]:
							opts[j][i].remove(k)
							
	sudoku, opts = sweep(sudoku, opts) # sweep everything
	sudoku, opts = uniques(sudoku, opts)
	
	for i in range(3): # look for twins in a block
		for j in range(3):
			# we are in a block
			foundpair = False
			pairs = []
			for k in range(3*i,3*i+3):
				for l in range(3*j,3*j+3):
					if len(opts[k][l])==2:
						if opts[k][l] in pairs:
							foundpair = opts[k][l]
							break
						else:
							pairs.append(opts[k][l])
			if foundpair:
				for k in range(3*i,3*i+3):
					for l in range(3*j,3*j+3):
						if opts[k][l] != foundpair:
							for m in foundpair:
								if m in opts[k][l]:
									opts[k][l].remove(m)
									
	sudoku, opts = sweep(sudoku, opts) # sweep everything
	sudoku, opts = uniques(sudoku, opts)
	return sudoku, opts

def solve(sudoku):
	#print "\n".join(["".join(str(i)) for i in sudoku])
	opts = [[range(1,10) for _ in range(9)] for _ in range(9)]

	# initial filling in opts
	for i in range(9):
		for j in range(9):
			if sudoku[i][j] != 0:
				opts[i][j] = []
				opts = crossout(opts, i, j, sudoku[i][j])

	for _ in range(20):
		sudoku, opts = twins(sudoku, opts) # look for twins
		if done(sudoku):
			break
	sudoku, opts = uniques(sudoku, opts)
	if check(sudoku,opts):
		if done(sudoku):
			global counter, tot
			counter += 1
			#print "done!"
			tot += sudoku[0][0]*100+sudoku[0][1]*10+sudoku[0][2]
		else:
			print "not done!"
			print "\n".join(["\t".join([str(j) if j!=0 else " " for j in i]) for i in sudoku])
			print "-"*70
	else:
		print "not valid!"
		print "\n".join(["\t".join([str(j) if j!=0 else " " for j in i]) for i in sudoku])
		print "-"*70
	

# read in the sudokus
with open("096_sudoku.txt", "r") as f:
	sudokus = []
	for line in f:
		if line[0]=="G":
			sudoku = []
			sudokus.append(sudoku)
		else:
			sudoku.append([int(i) for i in line.strip()])

for sudoku in sudokus:
	solve(sudoku)
print counter, tot

# 6 sudokus were not solved
# tried filling in a random number somewhere and see if it were valid