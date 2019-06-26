# https://leetcode.com/problems/number-of-islands/

# Time O(row * col)
# Space O(row * col)
# BFS Solution
class Solution:
    def boundaryChecker(self, arr, i, j):
        return not (i < 0 or j < 0 or i >= len(arr) or j >= len(arr[i]) or arr[i][j] == "0")

    def numIslands(self, grid) -> int:
        numIsland = 0
        queue = set()

        def _BFSTraverse(grid):

            while len(queue):
                i, j = queue.pop()
                grid[i][j] = "0"

                if self.boundaryChecker(grid, i - 1, j):
                    queue.add((i - 1, j))
                if self.boundaryChecker(grid, i + 1, j):
                    queue.add((i + 1, j))
                if self.boundaryChecker(grid, i, j + 1):
                    queue.add((i, j + 1))
                if self.boundaryChecker(grid, i, j - 1):
                    queue.add((i, j - 1))

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    queue.add((row, col))
                    numIsland += 1
                    _BFSTraverse(grid)

        return numIsland

# Time O(row * col)
# Space O(row * col)
# DFS Solution
# class Solution:
#     def boundaryChecker(self, arr, i, j):
#         return not (i < 0 or j < 0 or i >= len(arr) or j >= len(arr[i]) or arr[i][j] == "0")
#
#     def _DFSTraverse(self, grid, i, j):
#
#         if self.boundaryChecker(grid, i, j):
#             grid[i][j] = "0"
#             self._DFSTraverse(grid, i + 1, j)
#             self._DFSTraverse(grid, i - 1, j)
#             self._DFSTraverse(grid, i, j + 1)
#             self._DFSTraverse(grid, i, j - 1)
#
#     def numIslands(self, grid: List[List[str]]) -> int:
#         numIsland = 0
#         queue = []
#         for i in range(len(grid)):
#             for j in range(len(grid[i])):
#                 if grid[i][j] == "1":
#                     numIsland += 1
#                     self._DFSTraverse(grid, i, j)
#
#         return numIsland
