class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0
        
        i = 0
        while i < n:
            if haystack[i] == needle[0]:
                if haystack[i:i+m] == needle:
                    return i
            i+= 1
            
        return -1  
                