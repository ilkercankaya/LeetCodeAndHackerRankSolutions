# Tabulation solution
class Solution(object):
    def uniquePaths(self, m, n):

        dp = [[1] * n] * m

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i][j + 1] + dp[i + 1][j]

        return dp[0][0]

# Memoization With Recursion Solution
# class Solution(object):
#     def uniquePaths(self, m, n):
#         cache = {}
#         return self._uniquePaths(m, n, cache)
#
#     def _uniquePaths(self, m, n, dic, startX=0, startY=0):
#         def notPossible(x, y):
#             if x >= m or y >= n:
#                 return True
#             else:
#                 return False
#
#         def isAtEnd(r, c):
#             if r == m - 1 and c == n - 1:
#                 return True
#             else:
#                 return False
#
#         if notPossible(startX, startY):
#             return 0
#
#         if isAtEnd(startX, startY):
#             return 1
#
#         if (startX, startY) not in dic:
#             dic[(startX, startY)] = self._uniquePaths(m, n, dic, startX + 1, startY) + self._uniquePaths(m, n, dic,
#                                                                                                          startX,
#                                                                                                          startY + 1)
#
#         return dic[(startX, startY)]
