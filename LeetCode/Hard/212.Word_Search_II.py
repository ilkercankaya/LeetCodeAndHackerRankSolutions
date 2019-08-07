import collections


class TrieNode:
    def __init__(self):
        self.childrens = collections.defaultdict(TrieNode)
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, val):
        pCrawl = self.root

        for char in val:
            pCrawl = pCrawl.childrens[char]

        pCrawl.isWord = True

    def getWordsWithPrefix(self, coordinates, board, list, dir):
        pCrawl = self.root

        def backtrack(coord, crawler, word):
            row, col = coord
            if board[row][col] not in crawler.childrens:
                return

            crawler = crawler.childrens[board[row][col]]
            temp = board[row][col]
            board[row][col] = "*"

            if crawler.isWord:
                word.append(temp)
                list.append(''.join(word))
                word.pop()

                crawler.isWord = False

            for rowInc, colInc in dir:
                newRow = rowInc + row
                newCol = colInc + col

                if 0 <= newRow < len(board) and 0 <= newCol < len(board[0]) and board[newRow][newCol] != "*" and \
                        board[newRow][newCol] in crawler.childrens:
                    word.append(temp)
                    backtrack((newRow, newCol), crawler, word)
                    word.pop()

            board[row][col] = temp

        backtrack(coordinates, pCrawl, [])


class Solution:
    def findWords(self, board, words):
        trie = Trie()
        for word in words:
            trie.insert(word)

        results = []

        d = [(0, +1), (0, -1), (+1, 0), (-1, 0)]

        for i in range(len(board)):
            for j in range(len(board[i])):
                trie.getWordsWithPrefix((i, j), board, results, d)

        return results
