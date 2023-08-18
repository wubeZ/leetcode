class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]
        for i in range(1, len(prices)-1):
            temp = prices[i] - buy
            maxProfit = max(maxProfit, temp )
            buy = min(buy, prices[i])
            
        maxProfit = max(maxProfit, prices[-1] - buy)
        return maxProfit