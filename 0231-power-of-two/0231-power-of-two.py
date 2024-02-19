class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        
        num = bin(n)[2:]
        
        return 1 == num.count("1")