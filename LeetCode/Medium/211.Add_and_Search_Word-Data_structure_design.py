import collections
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isAWord = False
        self.maxChildNum = 0


class WordDictionary:

    def __init__(self):
        self.head = TrieNode()


    def addWord(self, word: str) -> None:
        pCrawl = self.head
        lenStr = len(word)
        for id, c in enumerate(word):
            pCrawl.maxChildNum = max(pCrawl.maxChildNum, lenStr - id)
            pCrawl = pCrawl.children[c]
        pCrawl.isAWord = True

    def search(self, word: str) -> bool:
        pCrawl = self.head
        lenStr = len(word)
        queue = [pCrawl]
        for id, c in enumerate(word):
            if c == ".":
                helper = []
                while queue:
                    mem = queue.pop(0)
                    for child in mem.children.values():
                        if child.maxChildNum >= lenStr - id - 1:
                            helper.append(child)
                queue = helper

            else:
                helper = []
                while queue:
                    mem = queue.pop(0)
                    if mem.children[c].maxChildNum >= lenStr - id - 1:
                        helper.append(mem.children[c])
                queue = helper

        for mem in queue:
            if mem.isAWord:
                return True
        return False


obj = WordDictionary()
obj.addWord("a")
obj.addWord("ab")
print(obj.search("a"))
