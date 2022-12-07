def move(stacks, direction):
    count = int(direction[6])
    start = int(direction[13])
    end = int(direction[18])

def part1():
    with open('input.txt') as input:
        lines = input.readlines()
    
    stacks = [[] for i in range(9)]
    for i, line in enumerate(lines):
        if i < 9:
            for j in range(9): # build stacks
                stacks[j].insert(0, line[j*4 + 1])
        elif i > 9:
            print(line, end='')
            move(stacks, line)
    
    for j in range(len(stacks[0])-1, -1, -1):
        print('')
        for i in range(len(stacks)):
            print(stacks[i][j], end=' ')


print(part1())