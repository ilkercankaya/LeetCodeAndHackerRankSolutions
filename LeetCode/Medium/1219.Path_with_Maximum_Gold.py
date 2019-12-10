class Solution:
    def getMaximumGold(self, grid) -> int:

        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        maxGold = 0
        currentGold = 0
        directions = [(0, +1), (0, -1), (+1, 0), (-1, 0)]

        def backtracker(currentIndex, grid):
            x, y = currentIndex
            nonlocal currentGold
            nonlocal maxGold
            currentGold += grid[x][y]
            maxGold = max(maxGold, currentGold)
            prevValue = grid[x][y]
            grid[x][y] = 0
            for xInc, yInc in directions:
                newX = x + xInc
                newY = y + yInc

                if 0 <= newX < len(grid) and 0 <= newY < len(grid[0]) and grid[newX][newY] != 0:
                    backtracker((newX, newY), grid)

            grid[x][y] = prevValue
            currentGold -= prevValue

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    backtracker((i, j), grid)

        return maxGold

s = Solution()
print(s.getMaximumGold(
[[0,0,34,0,5,0,7,0,0,0],[0,0,0,0,21,0,0,0,0,0],[0,18,0,0,8,0,0,0,4,0],[0,0,0,0,0,0,0,0,0,0],[15,0,0,0,0,22,0,0,0,21],[0,0,0,0,0,0,0,0,0,0],[0,7,0,0,0,0,0,0,38,0]]
))