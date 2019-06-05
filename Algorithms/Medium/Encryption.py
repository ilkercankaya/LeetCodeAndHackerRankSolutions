#!/bin/python3

import math
import os
import random
import re
import sys


# Encryption
# Complete the encryption function below.
def encryption(s):
    root = math.sqrt(len(s))

    top = math.ceil(root)
    bottom = math.floor(root)

    re_written = []
    for i in range(0, len(s), top):
        str_dummy = s[i: i + top]
        while len(str_dummy) != top:
            str_dummy += " "

        re_written.append(str_dummy)

    re_written = [*zip(*re_written)]

    final_string = ""
    for i in range(len(re_written)):
        dummy = ""

        for j in range(len(re_written[i])):
            if re_written[i][j] != " ":
                dummy += re_written[i][j]

        final_string += dummy + " "

    return final_string.strip()


if __name__ == '__main__':
    s = input()

    result = encryption(s)

    print(result)
