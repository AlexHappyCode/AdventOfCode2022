
with open('day6/input.txt') as input:
#with open('day6/example1.txt') as input:
    lines = input.readlines()

def first_x_unique(line, x):
    for i in range(len(line)):
        curStr = line[i]
        for j in range(i+1, len(line)):
            if len(curStr) == x:
                return (i + x, curStr)
            if line[j] not in curStr:
                curStr += line[j]
            else:
                break

print(first_x_unique(lines[0], 4))
print(first_x_unique(lines[0], 14))