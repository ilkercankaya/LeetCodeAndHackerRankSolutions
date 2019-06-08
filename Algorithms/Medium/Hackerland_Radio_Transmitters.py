#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hackerlandRadioTransmitters function below.
def findNextHouse(x, index, transmitter=False):
    # find the next house
    j = 1

    # reach the house
    while x[index + j] - x[index] <= k:
        j += 1

    # whether a install or a transmitter house
    if transmitter:
        j -= 1

    index += j

    return index


def hackerlandRadioTransmitters(x, k):
    x.sort()

    transmitters = 0
    index = 0
    last_transmitter_loc = 0
    try:
        while index < len(x):
            # find the transmitter house on the most right side to cover the max range
            index = findNextHouse(x, index, True)

            # needed for the last transmitter
            last_transmitter_loc = x[index]
            transmitters += 1

            # transmitter is set find the next non transmitted house
            index = findNextHouse(x, index)

    # last transmitters range will always cause an exception
    except IndexError:
        # the last indexed house is covered by the last transmitter or not
        if x[len(x) - 1] - last_transmitter_loc > k:
            transmitters += 1
        # needed for towns with only one transmitter
        elif transmitters == 0:
            transmitters += 1

    return transmitters


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    print(result)
