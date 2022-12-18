# advent of code 2022 day 9
import numpy as np

with open('day9.txt') as f:
    data = f.read().splitlines()


def uniqueSpotsTraveled(data):

    visited = set()
    visited.add((0, 0))  # starting with head
    uniqueSpots = 0
    head = np.array([0, 0])
    tail = np.array([0, 0])

    for i in range(len(data)):
        [direction, steps] = data[i].split()
        steps = int(steps)

        if direction == 'L':
            if (isTouching(head, tail)):
                visited.add(tail)
            else: # need to move tail
                pass

uniqueSpotsTraveled(data)

def isTouching(head, tail):
    adjacentSpots = [np.array([1, 0]), np.array([0, 1]), np.array(
        [-1, 0]), np.array([0, -1]), np.array([1, 1]), np.array([-1, -1]), np.array([0, 0]), np.array([1, -1])]

    if np.subtract(head, tail) in adjacentSpots:
        return True

# print(np.subtract(np.array([4, 1]), (np.array([2, 9]))))
