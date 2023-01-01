class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = list(s.split())
        if (len(arr) != len(pattern)) or (len(set(pattern)) != len(set(arr))):
            return False
        
        maps = {}
        
        for i in range(len(pattern)):
            if arr[i] not in maps:
                maps[arr[i]] = pattern[i]
            elif maps[arr[i]] != pattern[i]:
                return False
        
        return True
                
                
                