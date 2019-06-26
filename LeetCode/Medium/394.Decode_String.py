def decodeString(s: str) -> str:
    mapping = {
        "]": "["
    }

    stack = []
    for token in s:
        if not token in mapping:
            stack.append(token)
        else:

            word = []
            # peek stack
            while stack[-1] != mapping[token]:
                word.append(stack.pop())

            # pop "["
            stack.pop()
            word.reverse()
            word = ''.join(word)

            num = ""
            while len(stack) != 0 and stack[-1].isdigit():
                num += stack.pop()

            num = num[::-1]
            word = word *int(num)

            stack.append(word)

    result = ""

    while stack:
        result = stack.pop() + result

    return result

print(decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))