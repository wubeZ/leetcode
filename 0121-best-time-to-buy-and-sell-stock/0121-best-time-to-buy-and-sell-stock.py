class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]
        
        for i in range(1, len(prices)):
            profit = prices[i] - buy
            maxProfit = max(maxProfit, profit)
            buy = min(buy, prices[i])
            
        
        return maxProfit