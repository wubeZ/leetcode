class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        
        for i in range(len(s)): 
            for j in range(len(s), i, -1):  
                if len(res) >= j-i:
                    break
                elif s[i:j] == s[i:j][::-1]:
                    res = s[i:j]
                    break
        return res