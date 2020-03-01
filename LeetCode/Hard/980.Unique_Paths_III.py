class Solution:
    # time O(3^(R*C))
    def uniquePathsIII(self, grid) -> int:
        startCoords = None
        endCoords = None

        possibleSquareNum = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    startCoords = (i, j)
                elif grid[i][j] == 2:
                    endCoords = (i, j)
                elif grid[i][j] == 0:
                    possibleSquareNum += 1

        ans = 0

        def getNeighbours(currNode, visited):
            for dir in [(0, -1), (0, +1), (-1, 0), (+1, 0)]:
                newX, newY = currNode[0] + dir[0], currNode[1] + dir[1]
                newCoors = (newX, newY)
                if 0 <= newX < len(grid) and 0 <= newY < len(grid[0]) and newCoors not in visited and grid[newX][
                    newY] != -1:
                    yield (newX, newY)

        def backtrack(currNode, visited):
            if currNode == endCoords:
                if len(visited) == possibleSquareNum + 2:
                    nonlocal ans
                    ans += 1
                return

            for newCoors in getNeighbours(currNode, visited):
                visited.add(newCoors)
                backtrack(newCoors, visited)
                visited.remove(newCoors)

        start = set()
        start.add(startCoords)
        backtrack(startCoords, start)
        return ans
