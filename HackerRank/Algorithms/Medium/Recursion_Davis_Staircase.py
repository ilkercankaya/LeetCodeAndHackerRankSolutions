#!/bin/python3

import math
import os
import random
import re
import sys


# # TimeO(N), SpaceO(1), DP Bottom Up + Tabulation
def stepPerms(n):
    tab = [0, 1, 2, 4]
    for i in range(4, n + 1):
        res = tab[1] + tab[2] + tab[3]
        tab[1] = tab[2]
        tab[2] = tab[3]
        tab[3] = res

    if n < 4:
        return tab[n]

    return tab[3]

# TimeO(N), SpaceO(N), DP Bottom Up + Tabulation
# def stepPerms(n):
#     tab = [0, 1, 2, 4]
#     for i in range(4, n + 1):
#         tab.append(tab[i - 1] + tab[i - 2] + tab[i - 3])
#
#     return tab[n]

# # TimeO(N), SpaceO(N), DP Top Down + Memoization
# def stepPerms(n, memo = {}):
#
#     if n < 3:
#         return n
#     elif n == 3:
#         return 4
#
#     if n in memo:
#         return memo[n]
#     else:
#         memo[n] = stepPerms(n - 1, memo) + stepPerms(n - 2 ,memo) + stepPerms(n - 3 ,memo)
#         return memo[n]

# TimeO(3^N)
# def stepPerms(n):
#     if n < 3:
#         return n
#     elif n == 3:
#         return 4
#     else:
#         return stepPerms(n - 1) + stepPerms(n - 2) + stepPerms(n - 3)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
