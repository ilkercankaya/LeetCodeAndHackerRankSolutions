# DP Tabulation Solution
class Solution:
    def numSquares(self, n):
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            j = 1

            listofSolutions = []

            while j**2 <= i:
                listofSolutions.append(dp[i - j*j] + 1)
                j += 1


            dp[i] = min(listofSolutions)

        return dp[n]

# BFS Solution
# class Solution:
#     def numSquares(self, n):
#
#
#         squares = [i**2 for i in range(1, int(n**0.5)+1)]
#
#         step = 1
#         queue = {n}
#
#         while queue:
#             tempQueue = set()
#
#             for node in queue:
#                 for square in squares:
#                     if node-square == 0:
#                         return step
#                     if node < square:
#                         break
#                     tempQueue.add(node-square)
#
#             queue = tempQueue
#             step += 1


s = Solution()

print(s.numSquares(12))
