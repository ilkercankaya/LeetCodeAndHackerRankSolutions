from collections import defaultdict
import queue

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        wordToKeys = defaultdict(list)

        wordLength = len(beginWord)
        for word in wordList:
            for i in range(wordLength):
                wordToKeys[word[:i] + "*" + word[i + 1:]].append(word)

        visited = set()

        level = 1

        que = queue.Queue()
        que.put(beginWord)

        while que.qsize() > 0:

            level += 1

            for i in range(que.qsize()):
                curNode = que.get()
                for j in range(wordLength):
                    for neig in wordToKeys[curNode[:j] + "*" + curNode[j + 1:]]:
                        if neig in visited:
                            continue

                        if neig == endWord:
                            return level

                        visited.add(neig)
                        que.put(neig)
        return 0

s = Solution()
print(s.ladderLength("hit",
"cog",
["hot","dot","dog","lot","log","cog"]))