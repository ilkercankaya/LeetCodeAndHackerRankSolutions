# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from Queue import PriorityQueue


class Solution:
    def mergeKLists(self, lists):
        priorityQueue = PriorityQueue()

        for l in lists:
            if l:
                priorityQueue.put((l.val, l))

        head = ListNode(-1)
        pointer = head

        while not priorityQueue.empty():
            nodeVal, node = priorityQueue.get()
            pointer.next = ListNode(nodeVal)

            pointer = pointer.next
            node = node.next

            if node:
                priorityQueue.put((node.val, node))

        return head.next