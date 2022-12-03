import numpy as np

with open('input.txt') as input:
    lines = input.readlines()

elfMoney = [0, 0, 0]
curElfMoney = 0

for line in lines:
    if line == '\n':

        minIdx = np.argmin(elfMoney)
        elfMoney[minIdx] = max(curElfMoney, elfMoney[minIdx])
        curElfMoney = 0
        continue

    curElfMoney += int(line.split('\n')[0])
# calculate total
print(sum(elfMoney))