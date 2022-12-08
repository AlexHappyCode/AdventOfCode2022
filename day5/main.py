def move(stacks, direction):
    print(stacks)
    directions = direction.split()
    count = int(directions[1])
    start = int(directions[3])
    end = int(directions[5])

    crates = []
    curCount = 0
    while curCount < count:
        topmost = stacks[start-1].pop()
        if topmost == ' ': continue
        curCount += 1
        crates.append(topmost)
    
    # find next non empty crate
    nextEmpty = 0
    for i in range(len(stacks[end-1])-1, -1, -1):
        if stacks[end-1] != ' ': nextEmpty = i + 1
    stacks[end-1] = stacks[end-1][:nextEmpty] + crates# append top to other stack

def printStacks(stacks):
    for j in range(len(stacks[0])-1, -1, -1):
        print('')
        for i in range(len(stacks)):
            print(stacks[i][j], end=' ')


def part1():
    with open('input.txt') as input:
        lines = input.readlines()
    
    stacks = [[] for i in range(9)]
    for i, line in enumerate(lines):
        if i < 9:
            for j in range(9): # build stacks
                stacks[j].insert(0, line[j*4 + 1])
        elif i > 9:
            #printStacks(stacks)
            print(line, end='')
            move(stacks, line)
    

print(part1())