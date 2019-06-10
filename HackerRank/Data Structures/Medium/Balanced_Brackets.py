#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):

    stack = []

    # use stack to find the matching pairs
    try:
        for i in range(len(s)):
            if s[i] == "[":
                stack.append(s[i])
            elif s[i] == "{":
                stack.append(s[i])
            elif s[i] == "(":
                stack.append(s[i])
            elif s[i] == "]":
                if stack.pop() != "[":
                    return "NO"
            elif s[i] == "}":
                if stack.pop() != "{":
                    return "NO"
            elif s[i] == ")":
                if stack.pop() != "(":
                    return "NO"
    except IndexError:
        # tried to access the stack while it was empty
        return "NO"

    # could still have elements even after valid operations
    if len(stack) > 0:
        return "NO"

    return "YES"

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

        print(result)
