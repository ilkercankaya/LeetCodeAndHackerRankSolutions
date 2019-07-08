class TrieNode:
    def __init__(self):
        self.childrens = [None] * 26
        self.isAWord = False

class Trie:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        dummy = self.head

        for s in word:
            key = self.charToInt(s)
            if not dummy.childrens[key]:
                dummy.childrens[key] = TrieNode()
            dummy = dummy.childrens[key]

        dummy.isAWord = True

    def search(self, word: str) -> bool:
        dummy = self.head

        for s in word:
            key = self.charToInt(s)
            if not dummy.childrens[key]:
                return False
            else:
                dummy = dummy.childrens[key]

        return dummy.isAWord

    def startsWith(self, prefix: str) -> bool:
        dummy = self.head

        for s in prefix:
            key = self.charToInt(s)

            if not dummy.childrens[key]:
                return False
            else:
                dummy = dummy.childrens[key]
        return True

    def charToInt(self, c):
        return ord(c) - ord('a')

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

trie = Trie()

print(trie.startsWith("a"))