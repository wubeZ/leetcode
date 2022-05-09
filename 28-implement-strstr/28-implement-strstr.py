class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0
        
        def check(i):
            j = 0
            while j < m and haystack[i+j] == needle[j]:
                j += 1
            return j == m
                
        i = 0
        while i < (n-m +1):
            if check(i):
                return i
            i+= 1
            
        return -1  
                