import numpy as np

with open('input.txt') as f:
	rows = f.read().splitlines()

rows = [[int(digit) for digit in row] for row in rows ]
rows = np.array(rows)
totalVisibleTrees = rows.shape[0] + rows.shape[1] # add edges right away

test = []
for i in range(3):
	test.append([])
	for j in range(3):
		test[i].append(i +j + 1)

test = np.array(test)

print(test)
print(test[,1:,0:2])

for i in range(1, rows.shape[0]-1):
	row = rows[i]

	for j in range(1, row.shape[0]-1):
		leftSide = max(row[:j])
		rightSide = max(row[j+1:])
		above = max(rows[:i,j])