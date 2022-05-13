class Solution:
    def reverseBits(self, n: int) -> int:
        val = bin(n).replace("0b", "")
        val = val[::-1]
        val = val + (32 - len(val)) *'0'
        
        return int(val, 2)
        