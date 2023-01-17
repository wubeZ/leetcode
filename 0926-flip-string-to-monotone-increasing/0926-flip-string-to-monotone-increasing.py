class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zeros, ones = 0, 0
        for ch in s:
            if ch == "0":
                zeros += 1
                
        ones = len(s) - zeros
        curzeros, curones = 0, 0
        
        ans = min(ones, zeros)
        
        for i in range(len(s)):
            if s[i] == "1":
                leftzeros = zeros - curzeros
                ans = min(ans, leftzeros + curones)
                curones += 1
            else:
                leftzeros = zeros - curzeros
                ans = min(ans, leftzeros + curones)
                curzeros += 1
            
    
        return ans