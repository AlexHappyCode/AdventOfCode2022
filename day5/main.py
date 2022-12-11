def move(stacks, direction):
    printStacks(stacks)
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
    
    stacks[end-1].extend(crates)
    print(stacks[end-1])

def moveChunks(stacks, direction):
    printStacks(stacks)
    directions = direction.split()
    count = int(directions[1])
    start = int(directions[3])
    end = int(directions[5])

    crates = stacks[start-1][len(stacks[start-1]) - count:]
    stacks[start-1] = stacks[start-1][:len(stacks[start-1]) - count]
    stacks[end-1].extend(crates)


def printStacks(stacks):
    for i in range(len(stacks)):
        print(stacks[i])

def loadCrates():
    with open('input.txt') as input:
        lines = input.readlines()
    
    stacks = [[] for i in range(9)]
    for i, line in enumerate(lines):
        if i < 9:
            for j in range(9): # build stacks
                crate = line[j*4 + 1]
                if crate != ' ':
                    stacks[j].insert(0, line[j*4 + 1])
        elif i > 9:
            #printStacks(stacks)
            print(line, end='')
            moveChunks(stacks, line)
    # get top most of each stack

    res = ''
    for stack in stacks:
        res += stack[-1]

    return res
    

print(loadCrates())