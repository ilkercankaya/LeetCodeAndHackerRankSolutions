#!/bin/python3

import math
import os
import random
import re
import sys


# Pairs - O(N) solution

# Complete the pairs function below.
def pairs(k, arr):
    hashSet = set()
    count = 0
    for i in range(len(arr)):
        hashSet.add(arr[i])

    for i in range(len(arr)):
        # or if arr[i] - k in hashSet:
        if k + arr[i] in hashSet:
            count += 1

    return count


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    print(result)
