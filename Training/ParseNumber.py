from collections import deque
# Python does however include the collections.deque class
# which provides a double-ended queue and is implemented as a doubly-linked list internally.

def parseNumber(num):
    if num < 0:
        num *= -1

    if num == 0:
        return [0]

    result = deque()
    while num != 0:
        digit = num % 10
        result.appendleft(digit)
        num //= 10

    return result

print(parseNumber(12345))
print(parseNumber(1234))
print(parseNumber(123))
print(parseNumber(12))
print(parseNumber(1))
print(parseNumber(0))
print(parseNumber(-1))
print(parseNumber(-12))
print(parseNumber(-123))
print(parseNumber(-1234))
print(parseNumber(-12345))