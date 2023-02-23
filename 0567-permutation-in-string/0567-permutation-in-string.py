class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        counter2 = Counter(s1)
        counter = defaultdict(int)
        
        l = 0    
        for r in range(len(s2)):
            counter[s2[r]] += 1
            
            while (r - l + 1) >= len(s1):
                if counter == counter2:
                    return True
                counter[s2[l]] -= 1
                
                if counter[s2[l]] == 0:
                    del counter[s2[l]]            
                l += 1
            
        return False