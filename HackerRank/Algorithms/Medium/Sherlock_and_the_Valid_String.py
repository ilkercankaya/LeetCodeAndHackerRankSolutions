#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the isValid function below.
def isValid(s):
    dict = {}

    for i in range(len(s)):
        if s[i] not in dict:
            dict[s[i]] = 1
        else:
            dict[s[i]] += 1

    listStored = []
    for key, value in dict.items():
        listStored.append(value)

    # same freq for the max and min freqs
    if max(listStored) - min(listStored) == 0:
        return 'YES'

    # if max is one and the difference is one, the max could be decremented one
    if listStored.count(max(listStored)) == 1 and max(listStored) - min(listStored) == 1:
        return 'YES'

    # minimum freq is 1
    if listStored.count(min(listStored)) == 1 and min(listStored) == 1:
        # remove it and look for the result again
        listStored.remove(min(listStored))

        # the difference is now zero
        if max(listStored) - min(listStored) == 0:
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)
    print(result)
