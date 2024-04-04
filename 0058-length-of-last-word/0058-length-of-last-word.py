class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = list(s.strip().split())
        
        if not s:
            return 0
        return len(s[-1])