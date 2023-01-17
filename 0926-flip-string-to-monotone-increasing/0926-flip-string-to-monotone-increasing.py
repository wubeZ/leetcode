class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zeros = s.count('0')   
        ones = len(s) - zeros
        
        curzeros, curones = 0, 0
        
        ans = min(ones, zeros)
        
        for i in range(len(s)):
            leftzeros = zeros - curzeros
            ans = min(ans, leftzeros + curones)
            if s[i] == "1":
                curones += 1
            else:
                curzeros += 1
            
    
        return ans