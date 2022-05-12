class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:  
        s = bin(start ^ goal)
        return s.count("1")