class Solution:
    def combine(self, n: int, k: int):

        results = []
        path = []

        def backtrack(start):
            if len(path) == k:
                results.append(path[:])
                return

            for i in range(start, n + 1 - (k - len(path)) + 1):
                path.append(i)
                backtrack(i + 1)
                path.pop()

        backtrack(1)

        return results