#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxRegion function below.
def maxRegion(grid):
    maxReg = 0
    regionLength = 0
    dir = [(-1, 0), (+1, 0), (0, +1), (0, -1), (+1, +1), (-1, -1), (-1, +1), (+1, -1)]

    def dfs(i, j, grid):
        grid[i][j] = 0
        nonlocal regionLength
        regionLength += 1
        for row, col in dir:
            newRow = row + i
            newCol = col + j
            if newRow >= 0 and newCol >= 0 and newRow < len(grid) and newCol < len(grid[0]) and grid[newRow][
                newCol] == 1:
                dfs(newRow, newCol, grid)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                dfs(row, col, grid)
                maxReg = max(maxReg, regionLength)
                regionLength = 0

    return maxReg


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
