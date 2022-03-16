# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        self.ans = -1
        
        def finder(n, check):
            left, right = 1, n
            
            while left <= right:
                mid = left + (right - left)//2
                
                if not isBadVersion(mid):
                    left = mid + 1
                else:
                    self.ans = mid
                    if check:
                        right = mid - 1
                        
            return self.ans
        
        first = finder(n, True)
        
        return first