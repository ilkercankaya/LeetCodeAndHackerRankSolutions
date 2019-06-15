import json


class Solution:
    def maxProfit(self, prices):

        profit = 0

        if len(prices) == 0:
            return profit

        minStock = prices[0]

        for i in range(1, len(prices)):
            # if old price is higher sell and rebuy from current
            if prices[i - 1] > prices[i]:
                profit += prices[i - 1] - minStock
                minStock = prices[i]

            # if a smaller value is found buy it  from this price
            if prices[i] < minStock:
                minStock = prices[i]

            # if the stock is kept until last index is reached
            if i == len(prices) - 1 and minStock < prices[i]:
                profit += prices[i] - minStock

        return profit


def stringToIntegerList(input):
    return json.loads(input)


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            prices = stringToIntegerList(line);

            ret = Solution().maxProfit(prices)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()



