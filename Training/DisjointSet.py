class DisjointSetsForest:
    def __init__(self, N):
        # -1's are roots
        self.forest = [-1] * N

    # Time complexity O(N)
    # Speeds up the further search - hopefully
    def findWithPathCompression(self, a):
        if self.forest[a] < 0:
            return a
        else:
            self.forest[a] = self.findWithPathCompression(self.forest[a])
            return self.forest[a]

    # Time complexity O(N)
    def find(self, a):
        if self.forest[a] < 0:
            return a
        else:
            return self.find(self.forest[a])

    def unionRightToLeft(self, a, b):
        # considers cases where a and b are not roots
        # if a and b are not root time complexity becomes O(N) due to find
        aRoot = self.find(a)
        bRoot = self.find(b)

        # Stops Deadlocks
        if aRoot != bRoot:
            self.forest[bRoot] = aRoot

        print(self.forest)

    def unionBySize(self, a, b):
        # S[i] is –Size of the tree with root i. – indicates it is a root
        aRoot = self.find(a)
        bRoot = self.find(b)

        # Prevents cyclic graph
        if aRoot == bRoot:
            return

        # Compare Sizes
        if abs(self.forest[aRoot]) < abs(self.forest[bRoot]):
            self.forest[bRoot] += self.forest[aRoot]
            self.forest[aRoot] = bRoot
        else:
            self.forest[aRoot] += self.forest[bRoot]
            self.forest[bRoot] = aRoot

        print(self.forest)

    def unionByHeight(self, a, b):
        # S[i] is is –Height -1 of the tree with root i. – indicates it is a root
        # Height is the is the height of the tree rooted at i
        # -1 is necessary for trees of height 0.

        aRoot = self.find(a)
        bRoot = self.find(b)

        # Prevents cyclic graph
        if aRoot == bRoot:
            return

        # Compare Sizes
        if abs(self.forest[aRoot]) < abs(self.forest[bRoot]):
            self.forest[aRoot] = bRoot
        else:
            # equal size increment first one's size by one
            if self.forest[aRoot] == self.forest[bRoot]:
                self.forest[aRoot] -= 1
            # make bRoot child of aRoot
            self.forest[bRoot] = aRoot

        print(self.forest)


disjointset = DisjointSetsForest(10)

# Produces cyclic graph find will recurse out
disjointset.unionBySize(0, 4)
disjointset.unionBySize(2, 3)
disjointset.unionBySize(3, 0)
