def ReverseRecursive(str):
    if len(str) == 0:
        return str

    return ReverseRecursive(str[1:]) + str[0]


inp = input()

print(ReverseRecursive(inp))
