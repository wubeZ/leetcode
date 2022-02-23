class Solution:
    def countGoodNumbers(self, n: int) -> int:
        remainder = n % 2
        n -= remainder
        result = pow (20, n//2, 1000000007)
        
        if remainder == 1:
            result *= 5
            
        return result % 1000000007