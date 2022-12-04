import numpy as np

def part1(): #540
    with open('input.txt') as input:
        lines = input.readlines()

    total = 0
    for line in lines:
        line = line.strip('\n')
        first_elf, second_elf = line.split(',')
        first_elf = list(map(int, first_elf.split('-')))
        second_elf = list(map(int, second_elf.split('-')))

        if first_elf[0] <= second_elf[0] and first_elf[1] >= second_elf[1]:
            total += 1
        elif second_elf[0] <= first_elf[0] and second_elf[1] >= first_elf[1]:
            total += 1

    return total

def part2():
    with open('input.txt') as input:
        lines = input.readlines()

    total = 0
    for line in lines:
        line = line.strip('\n')
        first_elf, second_elf = line.split(',')

        first_elf_range = np.arange(int(first_elf.split('-')[0]), int(first_elf.split('-')[1]) + 1)
        second_elf_range = np.arange(int(second_elf.split('-')[0]), int(second_elf.split('-')[1]) + 1)

        first_set = set(first_elf_range)
        second_set = set(second_elf_range)

        overlapping = False
        for num in first_elf_range:
            if num in second_set:
                overlapping = True
                break
        if overlapping: 
            total += 1
            continue

        overlapping = False
        for num in second_elf_range:
            if num in first_set:
                overlapping = True
                break
        if overlapping: 
            total += 1

    return total

print(part1())
print(part2())