class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        results = []
        sizeDigits = len(digits)
        path = []

        def dfs(index):
            if len(path) == sizeDigits:
                results.append(''.join(path))
                return

            for char in mapping[digits[index]]:
                path.append(char)
                dfs(index + 1)
                path.pop()

        dfs(0)
        return results