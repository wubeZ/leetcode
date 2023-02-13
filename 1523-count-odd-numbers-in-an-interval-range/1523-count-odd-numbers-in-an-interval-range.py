class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans = 0
        
        if low %2 == 0 and high %2 == 0:
            ans = (high - low)//2
        else:
            ans = ((high - low)//2) + 1
        
        return ans