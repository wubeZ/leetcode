class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = list(map(str, s.split()))
        return len(s[-1])
        