class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = pow(2,31) - 1
        best = -1
        while left <= right:
            mid = left + (right - left)//2
            
            if mid**2 == x:
                return mid
            elif mid**2 > x:
                right = mid - 1
            else:
                best = mid
                left = mid + 1
                
        return best
            
            
            