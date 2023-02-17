class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = [0] * 26
        
        for ch in s:
            idx = ord(ch) - ord("a")
            counter[idx] += 1
        
        for i in range(len(s)):
            idx = ord(s[i]) - ord("a")
            if counter[idx] == 1:
                return i
        
        return -1
                