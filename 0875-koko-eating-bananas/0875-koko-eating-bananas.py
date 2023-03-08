class Solution:
    
    def checker(self, mid, piles, h):
        hours = 0
        for num in piles:
            hours += math.ceil(num / mid)

        return hours <= h
    
    def solve(self, piles, h):
        left = 0
        right = max(piles)
        
        while left + 1 < right:
            
            mid = left + (right - left)//2
            
            isValid = self.checker(mid, piles, h)
            
            if not isValid:
                left = mid
            else:
                right = mid
        
        
        return right
                

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        return self.solve(piles, h)
                