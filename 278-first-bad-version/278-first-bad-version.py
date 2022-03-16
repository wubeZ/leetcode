# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        first = 0
        while left <= right:
            mid = left + (right - left)//2
                
            if not isBadVersion(mid):
                left = mid + 1
            else:
                first = mid
                right = mid - 1
            
        
        return first
        
        
