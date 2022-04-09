class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = buy = 0
        profit = 0
        while buy < len(prices):
            sell = buy + 1
            while sell < len(prices) and prices[buy] < prices[sell]:
                profit = max(profit, prices[sell] - prices[buy])
                sell += 1
            buy = sell
        
        return profit
                
            
            
            