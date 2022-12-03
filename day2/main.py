from functools import reduce

# x - 1 y - 2 z -3 won 6 draw 3 0 lost

with open('input.txt') as input:
    lines = input.readlines()

def part1():
    total = 0
    for line in lines:
        myPlay = ord(line[2]) - 23 - ord('A') + 1
        theirPlay = ord(line[0]) - ord('A') + 1
        res = myPlay - theirPlay 
        if res == -2 or res == 1: 
            total += myPlay + 6 # i won
        if res == -1 or res == 2:
            total += myPlay
        if res == 0:
            total += myPlay + 3
    return total

# X - lose Y - draw Z - win
def part2():
    total = 0
    for line in lines:
        myPlay = None
        if line[2] == 'X': # I must lose
            if line[0] == 'A': myPlay = 'Z'
            if line[0] == 'B': myPlay = 'X'
            if line[0] == 'C': myPlay = 'Y'
        if line[2] == 'Y': myPlay = chr(ord(line[0]) + 23)
        if line[2] == 'Z': # I must win
            if line[0] == 'A': myPlay = 'Y'
            if line[0] == 'B': myPlay = 'Z'
            if line[0] == 'C': myPlay = 'X'

        myPlay = ord(myPlay) - 23 - ord('A') + 1
        theirPlay = ord(line[0]) - ord('A') + 1
        res = myPlay - theirPlay 
        if res == -2 or res == 1: 
            total += myPlay + 6 # i won
        if res == -1 or res == 2:
            total += myPlay
        if res == 0:
            total += myPlay + 3
    return total

print(part2())