class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) -1
        while left < right:
            if s[left] != s[right]:
                lside = s[left:right] 
                rside = s[left + 1:right + 1]
                return lside == lside[::-1] or rside == rside[::-1]
            left += 1
            right -= 1
        
        return True
                
            