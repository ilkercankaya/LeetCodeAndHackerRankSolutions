class Solution:
    def solve(self, board) -> None:

        R = len(board)

        if R == 0 or R == 1 or R == 2:
            return

        C = len(board[0])

        if C == 1 or C == 2:
            return

        travelStack = []

        for r in range(R):
            if board[r][0] == "O":
                travelStack.append((r, 0))
                board[r][0] = "F"

            if board[r][C - 1] == "O":
                travelStack.append((r, C - 1))
                board[r][C - 1] = "F"

        for c in range(len(board[0])):
            if board[0][c] == "O":
                travelStack.append((0, c))
                board[0][c] = "F"

            if board[R - 1][c] == "O":
                travelStack.append((R - 1, c))
                board[R - 1][c] = "F"

        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while travelStack:
            adjR, adjC = travelStack.pop(0)

            for direction in d:
                rowN = direction[0] + adjR
                colN = direction[1] + adjC

                if rowN >= 0 and rowN < R and colN >= 0 and colN < C and board[rowN][colN] == "O":
                    board[rowN][colN] = "F"
                    travelStack.append((rowN, colN))

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "F":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"


