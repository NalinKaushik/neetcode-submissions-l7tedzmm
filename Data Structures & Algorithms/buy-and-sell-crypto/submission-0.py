class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxprofit = 0
        for i in range(n-2,-1,-1):
            maxnum = max(prices[i+1:n])
            profit = maxnum - prices[i]
            maxprofit = max(maxprofit, profit)

        return maxprofit