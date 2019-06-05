#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the almostSorted function below.
def almostSorted(arr):
    i = 0
    j = len(arr) - 1
    fixed = False

    for k in range(len(arr)):
        # check if the ith next element is smaller than the first
        if arr[i] < arr[i + 1]:
            i += 1

        # check if the jth next element is smaller than the first
        if arr[j] > arr[j - 1]:
            j -= 1

    # have the indexes here try swapping
    arr[j], arr[i] = arr[i], arr[j]
    if sorted(arr) == arr:
        fixed = True
        print("yes")
        print("swap", i + 1, j + 1)

    else:
        # put the swapped back
        arr[j], arr[i] = arr[i], arr[j]

    # try reversing
    piece_of_arr = arr[i:j + 1]
    piece_of_arr.reverse()

    arr[i:j + 1] = piece_of_arr

    if sorted(arr) == arr:
        fixed = True
        print("yes")
        print("reverse", i + 1, j + 1)

    if not fixed:
        print("no")


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
