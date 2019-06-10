#!/bin/python3
import math
import os
import random
import re
import sys
import copy


# Ema's Supercomputer

def doesOverlap(one, two):
    for i in range(len(one)):
        try:
            two.index(one[i])
            # found a match
            return True
        except ValueError:
            pass

    return False


def boundaryChecker(row_count, column_count, i, j, substr):
    return i + substr < row_count and i - substr >= 0 and j + substr < column_count and j - substr >= 0


def plusCalculator(grid, sizes, coordinates, currentBoxCoord):
    size = 1

    substr = 1
    is_B_met = False
    i = currentBoxCoord[0]
    j = currentBoxCoord[1]
    box_coords = []
    box_coords.append([i, j])
    # while it could extend and pluses keeps forming
    while boundaryChecker(len(grid), len(grid[0]), i, j, substr) and not is_B_met:

        if not (grid[i + substr][j] == "G" and grid[i - substr][j] == "G"
                and grid[i][j + substr] == "G" and grid[i][j - substr] == "G"):
            is_B_met = True
        # four G found
        if not is_B_met:
            box_coords.append([i + substr, j])
            box_coords.append([i - substr, j])
            box_coords.append([i, j + substr])
            box_coords.append([i, j - substr])
            substr += 1
            size += 4

    sizes.append(size)
    coordinates.append(box_coords)


def removeBoundaries(coordinateList):
    # remove with respect to max row and max column
    coordinateList.remove(max(coordinateList, key=lambda p: p[0]))
    coordinateList.remove(max(coordinateList, key=lambda p: p[1]))
    coordinateList.remove(min(coordinateList, key=lambda p: p[0]))
    coordinateList.remove(min(coordinateList, key=lambda p: p[1]))

    return coordinateList


def removeOverlaps(first, second):
    while doesOverlap(first, second):
        # need to remove the boundaries
        if len(first) == len(second):
            first = removeBoundaries(first)
            second = removeBoundaries(second)
        elif len(first) > len(second):
            first = removeBoundaries(first)
        elif len(first) < len(second):
            second = removeBoundaries(second)

# Complete the twoPluses function below.
def twoPluses(grid):
    sizes = []
    coordinates = []

    # find all the boxes
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "G":
                plusCalculator(grid, sizes, coordinates, [i, j])

    # zip to try brute-force
    # 0 index is size, 1 index is coordinate array
    mapped = zip(sizes, coordinates)
    mapped = list(mapped)

    max_area = 0
    # brute force
    for i in range(len(mapped)):
        for j in range(len(mapped)):
            if i != j:
                # delete coordinates until they dont overlap
                if doesOverlap(mapped[i][1], mapped[j][1]):
                    first = copy.deepcopy(mapped[i][1])
                    second = copy.deepcopy(mapped[j][1])
                    removeOverlaps(first, second)
                    multiple = len(first) * len(second)
                    max_area = multiple if multiple > max_area else max_area
                else:
                    # no overlap just multiply
                    # if multiplicate is greater set new are
                    multiple = mapped[i][0] * mapped[j][0]
                    max_area = multiple if multiple > max_area else max_area

    return max_area


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    print(result)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
