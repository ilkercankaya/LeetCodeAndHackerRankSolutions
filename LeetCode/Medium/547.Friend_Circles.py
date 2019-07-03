class DisjointSetsForest:
    def __init__(self, N):
        # -1's are roots
        self.forest = [-1] * N
        self.setSize = N

    # Time complexity O(N)
    # Speeds up the further search - hopefully
    def findWithPathCompression(self, a):
        if self.forest[a] < 0:
            return a
        else:
            self.forest[a] = self.findWithPathCompression(self.forest[a])
            return self.forest[a]

    def unionByHeight(self, a, b):
        # S[i] is is –Height -1 of the tree with root i. – indicates it is a root
        # Height is the is the height of the tree rooted at i
        # -1 is necessary for trees of height 0.

        aRoot = self.findWithPathCompression(a)
        bRoot = self.findWithPathCompression(b)

        # Prevents cyclic graph
        if aRoot == bRoot:
            return

        self.setSize -= 1

        # Compare Sizes
        if abs(self.forest[aRoot]) < abs(self.forest[bRoot]):
            self.forest[aRoot] = bRoot
        else:
            # equal size increment first one's size by one
            if self.forest[aRoot] == self.forest[bRoot]:
                self.forest[aRoot] -= 1
            # make bRoot child of aRoot
            self.forest[bRoot] = aRoot


class Solution:
    def findCircleNum(self, M) -> int:
        unionFind = DisjointSetsForest(len(M))
        for i in range(len(M)):
            for j in range(0, i):
                if M[i][j] == 1:
                    unionFind.unionByHeight(i, j)

        return unionFind.setSize

S = Solution()
print(S.findCircleNum([[1,1,0],
 [1,1,0],
 [0,0,1]]))