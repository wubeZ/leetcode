class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        l, r = 0, len(s)-1 
        
        while l < r:
            if l < len(s) and r > -1 and s[l] in "aeiouAEIOU" and s[r] in "aeiouAEIOU":
                s[l],s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif l < len(s) and r > -1 and s[l] not in "aeiouAEIOU" and s[r] in "aeiouAEIOU":
                l += 1
            elif l < len(s) and r > -1 and s[l] in "aeiouAEIOU" and s[r] not in "aeiouAEIOU":
                r -= 1
            else:
                l += 1
                r -= 1
        
        return "".join(s)
                
        
            