class Solution:
    def exist(self, board, word: str) -> bool:
        if not word:
            return True

        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        sizeRow = len(board)
        sizeCol = len(board[0])
        wordSize = len(word)

        def backtracker(pos, index):
            row, col = pos
            for rowInc, colInc in dir:
                newRow = row + rowInc
                newCol = col + colInc

                if sizeRow > newRow >= 0 and sizeCol > newCol >= 0 and board[newRow][newCol] == word[index]:
                    if index == wordSize - 1:
                        return True
                    temp = board[newRow][newCol]
                    board[newRow][newCol] = "*"
                    if backtracker((newRow, newCol), index + 1):
                        board[newRow][newCol] = temp
                        return True
                    board[newRow][newCol] = temp

            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    temp = board[i][j]
                    board[i][j] = "*"
                    if wordSize == 1 or backtracker((i, j), 1):
                        return True
                    board[i][j] = temp

        return False
