class Solution:
    def knightDialer(self, N: int) -> int:
        cache = {}

        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]
        directions = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]

        def dp(N, r, c):
            if not (0 <= r <= 4 and 0 <= c < 4) or matrix[r][c] == -1 or N == 0:
                return 0

            if (N, r, c) in cache:
                return cache[(N, r, c)]

            ans = 0
            for xInc, yInc in directions:
                ans += dp(N - 1, r + xInc, c + yInc)

            cache[(N, r, c)] = ans

            return ans

        result = 0

        for i in range(4):
            for j in range(3):
                result += dp(N, i, j)

        return result
