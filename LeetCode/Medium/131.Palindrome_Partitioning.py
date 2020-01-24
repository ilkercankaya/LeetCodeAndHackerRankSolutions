class Solution:
    def partition(self, s):
        def dfs(start, path, res):
            if start >= len(s):
                res.append(path[:])
                return
            for i in range(start, len(s)):
                str = s[start:i + 1]
                if str == str[::-1]:
                    path.append(s[start:i + 1])
                    dfs(i + 1, path, res)
                    path.pop()
        res = []
        dfs(0, [], res)
        return res

s = Solution()
print(s.partition("aab"))