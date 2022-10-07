class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        counter = Counter(s1)
        
        for i in range(len(s2)-len(s1) + 1):
            newCounter = Counter(s2[i:i+len(s1)])
            if newCounter == counter:
                return True
        
        return False