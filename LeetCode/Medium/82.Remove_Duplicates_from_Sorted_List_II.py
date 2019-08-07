# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return head
        dummyHead = ListNode(float("inf"))

        dummyHead.next = head

        crawl = dummyHead
        while crawl and crawl.next and crawl.next.next:
            if crawl.next.val == crawl.next.next.val:
                nextNode = crawl.next.next.next
                while nextNode and nextNode.val == crawl.next.val:
                    nextNode = nextNode.next

                crawl.next = nextNode
            else:
                crawl = crawl.next

        return dummyHead.next