#!/bin/python3

import math
import os
import random
import re
import sys
import copy

# Patterns repeat after n = 4
# n = - ,1 ,2, 4
# n = 5 ,6 ,7, 8 are the same
# only solve the puzzle until n = 5 with hash maps for fast speed

# Complete the bomberMan function below.
def bomberMan(n, grid):
    # convert grid into char array to access with index
    grid_matrix = []
    for i in range(len(grid)):
        grid_matrix.append(list(grid[i]))

    # Hash Map Approach
    to_bomb = [[] for i in range(len(grid))]
    bomber_man_bombs = [[] for i in range(len(grid))]

    grid_one = None
    grid_two = None
    grid_three = None
    grid_four = None
    for i in range(1, n + 1, 1):

        if i > 5:
            break
        # first second has passed, bomberman does nothing, observe the grids
        if i == 1:
            for j in range(len(grid_matrix)):
                for k in range(len(grid_matrix[j])):
                    if grid_matrix[j][k] == "O":
                        # store indexes of initial bomb locations
                        to_bomb[j].append(k)

        # 2 second has passed
        elif i == 2 or (i > 3 and i % 2 == 0):
            bomber_man_bombs = [[] for i in range(len(grid))]
            for j in range(len(grid_matrix)):
                for k in range(len(grid_matrix[j])):
                    if grid_matrix[j][k] == ".":
                        # store indexes of initial bomb locations
                        grid_matrix[j][k] = "O"
                        bomber_man_bombs[j].append(k)
            if i == 2:
                grid_two = copy.deepcopy(grid_matrix)
            if i > 3 and i % 2 == 0:
                grid_four = copy.deepcopy(grid_matrix)

        # 3 second has passed
        elif i == 3 or (i > 3 and i % 2 == 1):
            for j in range(len(to_bomb)):
                for k in range(len(to_bomb[j])):

                    grid_matrix[j][to_bomb[j][k]] = "."

                    # Handle index exceptions with neighbour bombs
                    if j + 1 != len(grid):
                        grid_matrix[j + 1][to_bomb[j][k]] = "."

                        try:
                            bomber_man_bombs[j + 1].remove(to_bomb[j][k])
                        except ValueError:
                            pass

                    if j != 0:
                        grid_matrix[j - 1][to_bomb[j][k]] = "."

                        try:
                            bomber_man_bombs[j - 1].remove(to_bomb[j][k])
                        except ValueError:
                            pass

                    if to_bomb[j][k] + 1 != len(grid[0]):
                        grid_matrix[j][to_bomb[j][k] + 1] = "."

                        try:
                            bomber_man_bombs[j].remove(to_bomb[j][k] + 1)
                        except ValueError:
                            pass

                    if to_bomb[j][k] != 0:
                        grid_matrix[j][to_bomb[j][k] - 1] = "."

                        try:
                            bomber_man_bombs[j].remove(to_bomb[j][k] - 1)
                        except ValueError:
                            pass
            to_bomb = bomber_man_bombs

            if i == 3:
                grid_three = copy.deepcopy(grid_matrix)
            if i > 3 and i % 2 == 1:
                grid_one = copy.deepcopy(grid_matrix)


    # convert back to list with strings

    if n > 5:
        if n % 4 == 1:
            grid_matrix = grid_one

        if n % 4 == 2:
            grid_matrix = grid_two

        if n % 4 == 3:
            grid_matrix = grid_three

        if n % 4 == 0:
            grid_matrix = grid_four

    string_list = []

    for i in range(len(grid_matrix)):
        string_list.append(''.join(grid_matrix[i]))

    return string_list


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rcn = input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    print('\n'.join(result))
    # fptr.write('\n'.join(result))
    # fptr.write('\n')
    #
    # fptr.close()
