class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        
        total = 0
        count = 0
        
        for i, cost in enumerate(costs):
            if total + cost > coins:
                break
            total += cost
            count += 1
            
        return count