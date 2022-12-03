
with open('input.txt') as input:
    lines = input.readlines()


# hashmap to check

def part1():
    comp1letters = set()
    totalPoints = 0
    for line in lines:
        halfLen = int((len(line) - 1)/2) # -1 for newline character
        for i in range(halfLen):
            comp1letters.add(line[i])
        for i in range(halfLen, len(line) - 1):
            if line[i] in comp1letters:
                totalPoints += (ord(line[i]) - ord('a') + 1) if line[i].islower() else (ord(line[i]) - ord('A') + 27)
                break
        comp1letters.clear()
    return totalPoints

def part2():
    totalPoints = 0
    for i in range(0, len(lines), 3):
        firstLine = lines[i][:len(lines[i])-1] # to chop of new line
        secondLine = lines[i + 1][:len(lines[i+1])-1]
        thirdLine = lines[i + 2][:len(lines[i+2])-1]

        firstBag = set(firstLine)
        common = set()
        for c in secondLine:
            if c in firstBag:
                common.add(c)
            
        for c in thirdLine:
            if c in common:
                totalPoints += (ord(c) - ord('a') + 1) if c.islower() else (ord(c) - ord('A') + 27)
                break

    return totalPoints

print(part2())