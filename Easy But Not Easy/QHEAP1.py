# QHEAP1
# Not easy because removing an element requires some tricks and thinking. Can not be found easily on the internet  as well.

# Class by ilkercan Kaya: 10/06/2019
class MinBinaryHeap:
    def __init__(self):
        self.heap = []

    def getParentIndex(self, i):
        return (i - 1) // 2

    def getLeftChildIndex(self, i):
        return i * 2 + 1

    def getRightChildIndex(self, i):
        return i * 2 + 2

    def hasRightChildIndex(self, i):
        return self.getRightChildIndex(i) < len(self.heap)

    def hasLeftChildIndex(self, i):
        return self.getLeftChildIndex(i) < len(self.heap)

    def heapifyUp(self, pos):
        index = pos
        while self.getParentIndex(index) > -1:
            # everything is in order
            parentIndex = self.getParentIndex(index)

            if self.heap[parentIndex] < self.heap[index]:
                break
            else:
                # swap the elements
                self.heap[parentIndex], self.heap[index] = self.heap[index], self.heap[parentIndex]
            index = parentIndex

    def heapifyDown(self, pos):
        index = pos
        while self.hasLeftChildIndex(index):
            minChildIndex = self.getLeftChildIndex(index)

            if self.hasRightChildIndex(index) and self.heap[self.getRightChildIndex(index)] < self.heap[
                self.getLeftChildIndex(index)]:
                minChildIndex = self.getRightChildIndex(index)

            if self.heap[index] < self.heap[minChildIndex]:
                break
            else:
                self.heap[minChildIndex], self.heap[index] = self.heap[index], self.heap[minChildIndex]

            index = minChildIndex

    def insert(self, key):
        # insert to the end
        self.heap.append(key)

        # heapify up from the last index
        self.heapifyUp(len(self.heap) - 1)

    def removeTop(self):
        # take the last element into the first
        self.heap[0] = self.heap.pop()

        # heapify down
        self.heapifyDown(0)

    def removeElement(self, key):
        # take the last element into the first
        try:
            indexOfKey = self.heap.index(key)
            if indexOfKey == len(self.heap) - 1:
                self.heap.pop()
                return

            lastElement = self.heap.pop()
            self.heap[indexOfKey] = lastElement

            # heapify with respect to both heapify up and heapify down
            # important thing to note - after the swap only one of these methods are run fully

            """
            proof: after the swap if the node is greater than its parent it cannot be smaller than any of the child 
            since childs are smaller than the parent then it is either bubble down or nothing to be done
            """

            self.heapifyUp(indexOfKey)
            self.heapifyDown(indexOfKey)
        except ValueError:
            # looking for an key that doesnt exist in the binary heap
            return

    def peek(self):
        return self.heap[0]


if __name__ == '__main__':

    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    bheap = MinBinaryHeap()
    for i in range(len(queries)):
        if queries[i][0] == "1":
            bheap.insert(int(queries[i][1]))

        elif queries[i][0] == "2":
            bheap.removeElement(int(queries[i][1]))

        elif queries[i][0] == "3":
            print(bheap.peek())
