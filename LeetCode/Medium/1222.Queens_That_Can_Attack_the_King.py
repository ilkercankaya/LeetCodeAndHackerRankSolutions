class Solution:
    def queensAttacktheKing(self, queens, king):
        queensSet = set(list(map(lambda x: tuple(x), queens)))
        results = []

        def travelAmongBoard(x, y, dirInc):
            if (x, y) in queensSet:
                results.append([x, y])
                return

            xInc, yInc = dirInc
            newX, newY = x + xInc, y + yInc

            if 0 <= newX <= 7 and 0 <= newY <= 7:
                travelAmongBoard(newX, newY, dirInc)

            return

        directions = [(+1, 0), (-1, 0), (0, +1), (0, -1), (+1, +1), (+1, -1), (-1, +1), (-1, -1)]

        for dir in directions:
            travelAmongBoard(king[0], king[1], dir)

        return results
