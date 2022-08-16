class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for i in s:
            if counter[i] == 1:
                return s.index(i)
        
        return -1
                