class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if not s:
            return ""

        stack = []

        for char in s:
            if len(stack) == 0 or stack[-1][0] != char:
                stack.append((char, 1))
            else:
                stack.append((char, stack[-1][1] + 1))

            if stack[-1][1] == k:
                for i in range(k):
                    stack.pop()

        return ''.join([element[0] for element in stack])

