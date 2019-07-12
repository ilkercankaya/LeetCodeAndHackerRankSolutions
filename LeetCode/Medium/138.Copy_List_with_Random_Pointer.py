# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None

        nodeHash = {}

        crawl = head

        while crawl:

            if not crawl in nodeHash:
                nodeHash[crawl] = Node(crawl.val, None, None)

            if not crawl.random in nodeHash:
                nodeHash[crawl.random] = Node(crawl.random.val, None, None)

            if not crawl.next in nodeHash:
                nodeHash[crawl.next] = Node(crawl.next.val, None, None)

            if crawl.random:
                nodeHash[crawl].random = nodeHash[crawl.random]
            if crawl.next:
                nodeHash[crawl].next = nodeHash[crawl.next]

            crawl = crawl.next

        return nodeHash[head]
