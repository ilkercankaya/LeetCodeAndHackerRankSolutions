class Solution:
    def numDistinctIslands(self, grid) -> int:

        if not grid:
            return 0

        dir = [(0, -1), (-1, 0), (0, +1), (+1, 0)]
        seen = set()

        def dfs(x, y, x0, y0, currShape):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in seen and grid[x][y]:
                seen.add((x, y))
                currShape.append((x - x0, y - y0))
                for xInc, yInc in dir:
                    dfs(x + xInc, y + yInc, x0, y0, currShape)

        shapes = set()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    currShape = []
                    dfs(i, j, i, j, currShape)
                    if currShape:
                        shapes.add(tuple(currShape))

        return len(shapes)
