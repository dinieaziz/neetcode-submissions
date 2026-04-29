class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        O(n) - 2 pointers traversing only once
        
        Check for the latest profit and min price every iteration

        We loop once denoting the currentProfit and maxProfit.
        If we find a cheaper price, we update the initialBuy too.
        """

        initialBuy = prices[0] 
        maxProfit = 0

        for price in prices:
            maxProfit = max(maxProfit, price - initialBuy)
            initialBuy = min(initialBuy, price)

        return maxProfit