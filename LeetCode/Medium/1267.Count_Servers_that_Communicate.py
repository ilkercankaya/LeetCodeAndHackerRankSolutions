
class Solution:
    def countServers(self, grid):
        rowSum = list(map(sum, grid))
        colSum = list(map(sum, zip(*grid)))

        connected = sum(int(grid[i][j] and rowSum[i] + colSum[j] > 2) for i in range(len(grid)) for j in range(len(grid[i])))

        return connected


