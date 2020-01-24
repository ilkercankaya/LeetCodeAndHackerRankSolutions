class Solution:
    def generateParenthesis(self, n: int):
        if not n:
            return []

        results = []

        def backtrack(leftNum, rightNum, path):
            if leftNum == rightNum == 0:
                results.append(''.join(path))
                return

            if leftNum > 0:
                path.append("(")
                backtrack(leftNum - 1, rightNum, path)
                path.pop()

            if leftNum < rightNum:
                path.append(")")
                backtrack(leftNum, rightNum - 1, path)
                path.pop()


        backtrack(n, n, [])

        return results

s = Solution()
print(s.generateParenthesis(3))