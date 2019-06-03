# O(k) solution by me where k is the size of the obstacle array

#!/bin/python3

import math
import os
import random
import re
import sys

# Queen's Attack II
# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    min_col = 1
    max_col = n
    min_row = 1
    max_row = n


    # find right up most coordinate
    difference_right_up = n - max(r_q, c_q)
    right_upper_row = difference_right_up + r_q

    # find right up most coordinate
    difference_left_up = min(n - r_q , c_q - 1)
    left_upper_row = r_q + difference_left_up

    difference_right_down = min(r_q -1 , n - c_q)
    right_down_row = r_q - difference_right_down

    # find left down most coordinate
    left_down_row = r_q - min(r_q, c_q) + 1

    for i in range(len(obstacles)):
        # find min column
        if obstacles[i][0] == r_q  or obstacles[i][1] == c_q :
            print(obstacles[i][0], obstacles[i][1])

        if obstacles[i][0] == r_q and obstacles[i][1] < c_q and obstacles[i][1] > min_col:
            min_col = obstacles[i][1] + 1

        # find max column
        if obstacles[i][0] == r_q and obstacles[i][1] > c_q and obstacles[i][1] < max_col:
            max_col = obstacles[i][1] - 1

        # find min row
        if obstacles[i][1] == c_q and obstacles[i][0] < r_q and obstacles[i][1] > min_row:
            min_row = obstacles[i][0] + 1

        # find max row
        if obstacles[i][1] == c_q and obstacles[i][0] > r_q and obstacles[i][1] < max_row:
            max_row = obstacles[i][0] - 1

        # diagonal right upper row
        if abs(obstacles[i][1] - c_q) == abs(obstacles[i][0] - r_q) and obstacles[i][0] > r_q and obstacles[i][1] > c_q and \
                obstacles[i][0] < right_upper_row:
            right_upper_row = obstacles[i][0] - 1

        # diagonal left upper row
        if abs(obstacles[i][1] - c_q) == abs(obstacles[i][0] - r_q) and obstacles[i][0] > r_q and obstacles[i][1] < c_q and \
                obstacles[i][0] < left_upper_row:
            left_upper_row = obstacles[i][0] - 1

        # diagonal right down row
        if abs(obstacles[i][1] - c_q) == abs(obstacles[i][0] - r_q) and obstacles[i][0] < r_q and obstacles[i][1] > c_q and \
                obstacles[i][0] > right_down_row:
            right_down_row = obstacles[i][0] + 1

        # diagonal left down row
        if abs(obstacles[i][1] - c_q) == abs(obstacles[i][0] - r_q) and obstacles[i][0] < r_q and obstacles[i][1] < c_q and \
                obstacles[i][0] > left_down_row:
            left_down_row = obstacles[i][0] + 1

    # find the available moves
    lateral = max_row - min_row
    vertical = max_col - min_col

    right_diognal = abs(right_upper_row - left_down_row)
    left_diognal = abs(left_upper_row - right_down_row)

    return lateral + vertical + right_diognal + left_diognal

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(result)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
