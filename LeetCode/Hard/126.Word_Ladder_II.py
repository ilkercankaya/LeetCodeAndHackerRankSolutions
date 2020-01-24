from collections import defaultdict, deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        res = []
        ladder = defaultdict(list)

        for word in wordList:
            for i in range(len(beginWord)):
                ladder[word[:i] + "*" + word[i + 1:]].append(word)

        childs = defaultdict(set)

        q = deque()
        q.append(beginWord)

        visited = set()
        visited.add(beginWord)

        targetReached = False
        while len(q) > 0:
            dummy = set()
            for i in range(len(q)):
                cur = q.popleft()

                for j in range(len(beginWord)):
                    for neig in ladder[cur[:j] + "*" + cur[j + 1:]]:
                        if neig not in visited:
                            q.append(neig)
                            childs[cur].add(neig)
                            # need dummy for cases where two nodes share the same neighbour but a node that is parent of
                            # them should not add its children to the queue for repeated processing
                            dummy.add(neig)
                            if neig == endWord:
                                targetReached = True

            visited = visited.union(dummy)
            if targetReached:
                break


        def dfs(curWord, path, res):
            if curWord == endWord:
                res.append(path[::])

            for child in childs[curWord]:
                path.append(child)
                dfs(child, path, res)
                path.pop()

        dfs(beginWord, [beginWord], res)
        return res

s = Solution()
print(s.findLadders("red"
,"tax",
["ted","tex","red","tax","tad","den","rex","pee"]))
