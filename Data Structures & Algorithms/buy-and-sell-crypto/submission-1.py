class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxprofit, maxnum = 0, prices[-1]
        for i in range(n-2,-1,-1):
            profit = maxnum - prices[i]
            maxprofit = max(maxprofit, profit)
            maxnum = max(maxnum, prices[i])

        return maxprofit