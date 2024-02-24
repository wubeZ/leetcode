class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count("1")
        
        leng = len(s) 
        
        ans = "1" * (ones - 1) + "0" * (leng - ones) + "1"
        
        return ans