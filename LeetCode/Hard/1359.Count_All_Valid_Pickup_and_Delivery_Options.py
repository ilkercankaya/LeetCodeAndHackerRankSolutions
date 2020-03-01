class Solution:
    def countOrders(self, n: int) -> int:
        count = 0
        def helper(pickUpCtr, deliveryCtr):
            if pickUpCtr < 0 or deliveryCtr < 0 or pickUpCtr > deliveryCtr:
                return

            nonlocal count
            if pickUpCtr == 0 and deliveryCtr == 0:
                count += 1
                return

            if pickUpCtr == deliveryCtr:
                helper(pickUpCtr - 1, deliveryCtr)
            elif pickUpCtr <= deliveryCtr:
                helper(pickUpCtr - 1, deliveryCtr)
                helper(pickUpCtr, deliveryCtr - 1)


        helper(n,n)
        return count * n
    
s = Solution()
print(s.countOrders(2))