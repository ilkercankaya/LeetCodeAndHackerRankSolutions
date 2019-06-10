#!/bin/python3

import os
import sys


# Game of Two Stacks
# Complete the twoStacks function below.
#
def twoStacks(x, a, b):
    sum = 0
    i = 0
    j = 0

    # initially ignore the first stack and find the index
    while i < n and sum + a[i] <= x:
        sum += a[i]
        i += 1

    count = i

    # keep adding from second stack until fist or second stack is finished
    while j < len(b) and i >= 0:
        sum += b[j]
        j += 1

        # delete an element from the second stack until sum criteria is not exceed
        while sum > x and i > 0:
            i -= 1
            sum -= a[i]

        # check if the new count is greater than the old
        if sum <= x and i + j > count:
            count = i + j

    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)

        # fptr.write(str(result) + '\n')
        print(result)
    # fptr.close()
