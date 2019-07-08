class TrieNode:
    def __init__(self):
        self.childrens = [None] * 26
        self.value = 0


class MapSum:

    def __init__(self):
        self.head = TrieNode()
        self.keyDict = {}

    def charToInt(self, a):
        return ord(a) - ord('a')

    def insert(self, key: str, val: int) -> None:
        prevVal = self.keyDict.get(key, 0)
        inc = val - prevVal
        self.keyDict[key] = val

        pCrawl = self.head
        for c in key:
            charKey = self.charToInt(c)
            if not pCrawl.childrens[charKey]:
                pCrawl.childrens[charKey] = TrieNode()
            pCrawl = pCrawl.childrens[charKey]
            pCrawl.value += inc

    def sum(self, prefix: str) -> int:
        pCrawl = self.head

        for c in prefix:
            key = self.charToInt(c)
            if not pCrawl.childrens[key]:
                return 0
            pCrawl = pCrawl.childrens[key]

        return pCrawl.value


# Your MapSum object will be instantiated and called as such:


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
mapSum = MapSum()
mapSum.insert("a",3)
print(mapSum.sum("ap"))
