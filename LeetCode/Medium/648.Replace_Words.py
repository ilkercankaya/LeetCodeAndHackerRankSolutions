class TrieNode:

    # Trie node class
    def __init__(self):
        self.children = [None] * 26
        self.total = 0
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):

        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def _charToIndex(self, ch):

        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case

        return ord(ch) - ord('a')

    def prefixSubstitute(self, word):
        pCrawl = self.root

        length = len(word)
        for level in range(length):
            index = self._charToIndex(word[level])

            if pCrawl.isEndOfWord:
                return word[0:level]

            if not pCrawl.children[index]:
                return None

            pCrawl = pCrawl.children[index]

    def insert(self, key):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
            pCrawl.total += 1

            # mark last node as leaf
        pCrawl.isEndOfWord = True


class Solution:
    def replaceWords(self, dicty, sentence):
        trie = Trie()

        # insert every word in dict
        for i in range(len(dicty)):
            trie.insert(dicty[i])

        listInput = sentence.split(" ")

        # search for the roots
        for i in range(len(listInput)):
            root = trie.prefixSubstitute(listInput[i])

            if root:
                listInput[i] = root

        return ' '.join(listInput)
