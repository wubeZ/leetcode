class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cursell = '-inf'
        curbuy = '-inf'
        nextsell = 0
        nextbuy = 0
        
        
        for i in range(len(prices)-1,-1,-1):
            cursell = max(prices[i] - fee + nextbuy, nextsell)
            curbuy = max(- prices[i] + nextsell , nextbuy)
            
            nextsell = cursell
            nextbuy = curbuy
            
        return nextbuy