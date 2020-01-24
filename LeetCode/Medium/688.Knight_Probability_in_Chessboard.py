class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:

        directions = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]

        def dp(K, r, c):

            if (K, r, c) in cache:
                return cache[(K, r, c)]

            if K == 0:
                return 1

            sumOfWays = 0
            for xInc, yInc in directions:
                if (0 <= r + xInc < N and 0 <= c + yInc < N):
                    sumOfWays += dp(K - 1, r + xInc, c + yInc)

            cache[(K, r, c)] = sumOfWays

            return sumOfWays

        cache = {}
        ans = dp(K, r, c)

        return ans / (8 ** K)

s = Solution()
print(s.knightProbability(8,30,6,4))
print(s.knightProbability(3,2,0,0))