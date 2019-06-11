# QHEAP1
# Not easy because removing an element requires some tricks and thinking. Can not be found easily on the internet  as well.


# Heap Sort by ilkercan Kaya: 11/06/2019
def heapSortDescending(array):
    # only uses its methods
    heap = MinBinaryHeap()
    heap.heap = array

    # build a heap from the given array
    for i in range(len(array) // 2 - 1):
        heap.heapifyDown(i)

    # keep a sorted partition and a non sorted - keep on swapping the root with the last element
    for i in range(len(array) - 1, 0, -1):
        heap.heap[i], heap.heap[0] = heap.heap[0], heap.heap[i]  # swap
        heap.heapifyDownWithSize(0, i)

    return heap.heap


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

    def hasRightChildIndex(self, i, size):
        return self.getRightChildIndex(i) < size

    def hasLeftChildIndex(self, i, size):
        return self.getLeftChildIndex(i) < size

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

    def heapifyDownWithSize(self, pos, size):
        index = pos
        count = 0
        while self.hasLeftChildIndex(index, size):
            minChildIndex = self.getLeftChildIndex(index)

            if self.hasRightChildIndex(index, size) and self.heap[self.getRightChildIndex(index)] < self.heap[
                self.getLeftChildIndex(index)]:
                minChildIndex = self.getRightChildIndex(index)

            if self.heap[index] < self.heap[minChildIndex]:
                break
            else:
                self.heap[minChildIndex], self.heap[index] = self.heap[index], self.heap[minChildIndex]

            count += 1

            index = minChildIndex

    def heapifyDown(self, pos):
        index = pos
        while self.hasLeftChildIndex(index, len(self.heap)):
            minChildIndex = self.getLeftChildIndex(index)

            if self.hasRightChildIndex(index, len(self.heap)) and self.heap[self.getRightChildIndex(index)] < self.heap[
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

            # heapify with respect to heapify down
            """
            proof: ONLY HEAPIFYDOWN is required. Proof: If a node at a level is swapped with the last node 
            since the last node is greater than the current node,
            it is guranteed that the new value is always bigger than its parent.
            """
            self.heapifyDown(indexOfKey)
        except ValueError:
            # looking for an key that doesnt exist in the binary heap
            return

    def peek(self):
        return self.heap[0]


if __name__ == '__main__':

    print(heapSortDescending([1, 6, 3, 5, 9, 4]))
    print(heapSortDescending([2, 1, 9, 12, 15, 19, 3]))
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
