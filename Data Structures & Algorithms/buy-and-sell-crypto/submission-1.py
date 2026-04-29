class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Buy low, sell high and must be towards the future - dynamic programming
        We need to keep track of the maximum profit - max()
        We need to keep track of the lowest price to buy - min()

        time:  0(n)
        space: 0(1)
        """

        minBuy = prices[0]
        maxProfit = 0

        for i in range(len(prices)):
            maxProfit = max(maxProfit, prices[i] - minBuy)
            minBuy = min(minBuy, prices[i])

        return maxProfit