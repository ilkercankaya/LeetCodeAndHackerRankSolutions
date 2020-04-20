class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs) -> bool:
        if len(words1) != len(words2):
            return False

        indexMap = {}

        def mapToInt():
            init = 0
            for pair in pairs:
                for word in pair:
                    if word not in indexMap:
                        indexMap[word] = init
                        init += 1

        mapToInt()

        parents = [-1] * len(pairs) * 2

        def find(x):
            if parents[x] < 0:
                return x

            parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            parX, parY = find(x), find(y)

            if parX == parY:
                return

            if abs(parents[parY]) > abs(parents[parX]):
                parents[parY] = parX
            elif abs(parents[parY]) < abs(parents[parX]):
                parents[parX] = parY
            else:
                parents[parX] = parY
                parents[parY] -= 1

        for one, two in pairs:
            union(indexMap[one], indexMap[two])

        return all(
            [start == end or start in indexMap and end in indexMap and find(indexMap[start]) == find(indexMap[end]) for
             start, end in zip(words1, words2)])

s = Solution()
print(s.areSentencesSimilarTwo(["this","summer","thomas","get","really","very","rich","and","have","any","actually","wonderful","and","good","truck","every","morning","he","drives","an","extraordinary","truck","around","the","nice","city","to","eat","some","extremely","extraordinary","food","as","his","meal","but","he","only","entertain","an","few","well","fruits","as","single","lunch","he","wants","to","eat","single","single","and","really","healthy","life"],
["this","summer","thomas","get","very","extremely","rich","and","possess","the","actually","great","and","wonderful","vehicle","every","morning","he","drives","unique","extraordinary","automobile","around","unique","fine","city","to","drink","single","extremely","nice","meal","as","his","super","but","he","only","entertain","a","few","extraordinary","food","as","some","brunch","he","wants","to","take","any","some","and","really","healthy","life"],
[["good","nice"],["good","excellent"],["good","well"],["good","great"],["fine","nice"],["fine","excellent"],["fine","well"],["fine","great"],["wonderful","nice"],["wonderful","excellent"],["wonderful","well"],["wonderful","great"],["extraordinary","nice"],["extraordinary","excellent"],["extraordinary","well"],["extraordinary","great"],["one","a"],["one","an"],["one","unique"],["one","any"],["single","a"],["single","an"],["single","unique"],["single","any"],["the","a"],["the","an"],["the","unique"],["the","any"],["some","a"],["some","an"],["some","unique"],["some","any"],["car","vehicle"],["car","automobile"],["car","truck"],["auto","vehicle"],["auto","automobile"],["auto","truck"],["wagon","vehicle"],["wagon","automobile"],["wagon","truck"],["have","take"],["have","drink"],["eat","take"],["eat","drink"],["entertain","take"],["entertain","drink"],["meal","lunch"],["meal","dinner"],["meal","breakfast"],["meal","fruits"],["super","lunch"],["super","dinner"],["super","breakfast"],["super","fruits"],["food","lunch"],["food","dinner"],["food","breakfast"],["food","fruits"],["brunch","lunch"],["brunch","dinner"],["brunch","breakfast"],["brunch","fruits"],["own","have"],["own","possess"],["keep","have"],["keep","possess"],["very","super"],["very","actually"],["really","super"],["really","actually"],["extremely","super"],["extremely","actually"]]))
