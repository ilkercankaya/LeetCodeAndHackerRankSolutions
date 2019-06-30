# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        iterOne = l1
        iterTwo = l2
        dummy = ListNode(0)
        curr = dummy

        carry = 0
        while iterOne is not None or iterTwo is not None:
            x = iterOne.val if iterOne else 0
            y = iterTwo.val if iterTwo else 0

            sum = carry + x + y

            carry = sum // 10

            curr.next = ListNode(sum % 10)
            curr = curr.next

            iterOne = iterOne.next if iterOne else None
            iterTwo = iterTwo.next if iterTwo else None

        if carry > 0:
            curr.next = ListNode(carry)

        return dummy.next