class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        counter = [0] * 26
        
        for i in range(len(s)):
            idx = ord(s[i]) - 97
            if counter[idx] == 0:
                counter[idx] = i+1
            else:
                prev = counter[idx]
                counter[idx] = i+1 - prev - 1
                if counter[idx] != distance[idx]:
                    return False
        
        return True
    
        
            