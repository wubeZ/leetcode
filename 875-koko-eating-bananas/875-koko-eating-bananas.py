class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def helper(mid):
            n = len(piles)
            prefix = 0
            for i in range(n):
                prefix += (math.ceil(piles[i]/mid))
            return prefix <= h
        
        ans = 0
        l, r = 1, max(piles)
        while l <= r:
            mid = l + (r - l)//2
            if helper(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
                
        return ans