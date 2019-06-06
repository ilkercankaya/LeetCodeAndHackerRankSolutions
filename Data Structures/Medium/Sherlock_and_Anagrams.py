#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    hashMap = {}
    count = 0
    # find all substrings - O(N^2)
    for i in range(len(s)):
        for j in range(i, len(s)):
            substr = s[i:j + 1]
            sorted_str = ''.join(sorted(substr))
            if sorted_str in hashMap:
                hashMap[sorted_str] += 1
            else:
                hashMap[sorted_str] = 1

    for key, item in hashMap.items():
        if hashMap[key] > 1:
            count += math.factorial(hashMap[key]) // (math.factorial(2) * math.factorial(hashMap[key] - 2))

    return count


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(result)
