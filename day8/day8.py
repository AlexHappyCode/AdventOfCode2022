import os
import numpy as np
from functools import reduce

print(os.getcwd())

def getTotalVisibleTrees():
    with open('day8.txt') as f:
        rows = f.read().splitlines()


    rows = [[int(digit) for digit in row] for row in rows]

    rows = np.array(rows)
    totalVisibleTrees = rows.shape[0]*2 + rows.shape[1]*2 - 4 # add edges right away

    for i in range(1, rows.shape[0]-1):
        row = rows[i]

        for j in range(1, row.shape[0]-1):
            leftSide = max(row[:j])
            rightSide = max(row[j+1:])
            above = max(rows[:i,j])
            below = max(rows[i+1:,j])

            tree = row[j]
            if tree > leftSide or tree > rightSide or tree > above or tree > below:
                totalVisibleTrees += 1

    return totalVisibleTrees

def highestScenicScore():
    with open('day8.txt') as f:
        rows = f.read().splitlines()
    rows = [[int(digit) for digit in row] for row in rows]
    rows = np.array(rows)
    maxScore = 0
    for i in range(1, rows.shape[0]):
        row = rows[i]
        for j in range(1, row.shape[0]):
            tree = row[j]
            scores = []
            scoreUp = 0
            for k in range(i-1, -1, -1):
                if rows[k, j] < tree:
                    scoreUp += 1
                else:
                    scoreUp += 1
                    break
            scores.append(scoreUp)

            scoreDown = 0
            for k in range(i+1, rows.shape[0]):
                if rows[k, j] < tree:
                    scoreDown += 1
                else:
                    scoreDown += 1
                    break
            scores.append(scoreDown)
            scoreLeft = 0
            for k in range(j-1, -1, -1):
                if rows[i, k] < tree:
                    scoreLeft += 1
                else:
                    scoreLeft += 1
                    break
            
            scores.append(scoreLeft)
            scoreRight = 0
            for k in range(j+1, rows.shape[1]):
                if rows[i, k] < tree:
                    scoreRight += 1
                else:
                    scoreRight += 1
                    break
            scores.append(scoreRight)
            score = reduce(lambda x, y: x*y, scores)
            maxScore = max(maxScore, score)
    return maxScore

print(highestScenicScore())