class Solution:
    def isValidSudoku(self, board) -> bool:
        for i in range(len(board)):
            rowSet = set()
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rowSet:
                    return False
                rowSet.add(board[i][j])

        for j in range(len(board[0])):
            colSet = set()
            for i in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in colSet:
                    return False
                colSet.add(board[i][j])

        for rowk in range(0, 9, 3):
            for colk in range(0, 9, 3):
                threeByThreeSet = set()
                for i in range(rowk, rowk + 3):
                    for j in range(colk, colk + 3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in threeByThreeSet:
                            return False
                        threeByThreeSet.add(board[i][j])
        return True


s = Solution()
print(s.isValidSudoku([[".", ".", ".", ".", "5", ".", ".", "1", "."], [".", "4", ".", "3", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", "3", ".", ".", "1"], ["8", ".", ".", ".", ".", ".", ".", "2", "."],
                       [".", ".", "2", ".", "7", ".", ".", ".", "."], [".", "1", "5", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", "2", ".", ".", "."], [".", "2", ".", "9", ".", ".", ".", ".", "."],
                       [".", ".", "4", ".", ".", ".", ".", ".", "."]]))
