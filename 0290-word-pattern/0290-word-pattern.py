class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = list(s.split())
        if len(arr) != len(pattern):
            return False
        
        pattern_map = {}
        s_map = {}
        
        for i in range((len(pattern))):
            pattern_map[pattern[i]] = arr[i]
            s_map[arr[i]] = pattern[i]
        
        for key in s_map:
            if pattern_map[s_map[key]] != key:
                return False
            
        for key in pattern_map:
            if s_map[pattern_map[key]] != key:
                return False
        
        for i in range(len(pattern)):
            if pattern_map[pattern[i]] != arr[i]:
                return False
        
        return True
                
                
                