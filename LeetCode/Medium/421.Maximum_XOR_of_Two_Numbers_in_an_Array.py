import collections


class TrieNode:
    def __init__(self):
        self.childrens = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, val):
        pCrawl = self.root
        for char in val:
            pCrawl = pCrawl.childrens[char]

    def query(self, val):
        pCrawl = self.root
        l = []
        for char in val:
            opposite = "0" if char == "1" else "1"
            if opposite in pCrawl.childrens:
                pCrawl = pCrawl.childrens[opposite]
                l.append(opposite)
            else:
                pCrawl = pCrawl.childrens[char]
                l.append(char)
        return int(''.join(l), 2) ^ int(val, 2)


class Solution:
    def findMaximumXOR(self, nums) -> int:
        maxRes = 0
        trie = Trie()
        for num in nums:
            num = '{:032b}'.format(num)
            maxRes = max(maxRes, trie.query(num))
            trie.insert(num)

        return maxRes

    def findMaximumXORContinous(self, nums) -> int:
        maxRes = 0
        pre = 0
        trie = Trie()
        for num in nums:
            pre = pre ^ num
            num = '{:032b}'.format(pre)
            trie.insert(num)
            maxRes = max(maxRes, trie.query(num))

        return maxRes

s = Solution()
print(s.findMaximumXORContinous([2, 5, 3, 7, 7, 7, 0, 5, 3, 8, 2, 6, 4]))

