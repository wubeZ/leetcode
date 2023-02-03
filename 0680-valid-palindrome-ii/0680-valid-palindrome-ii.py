class Solution:
    def validPalindrome(self, s: str) -> bool:
        reverse_s = s[::-1]
        if s == reverse_s:
            return True
        
        for i in range(len(s)):
            if s[i] != reverse_s[i]:
                deleted_s = s[:i] + s[i+1:]
                deleted_reverse = reverse_s[:i] + reverse_s[i+1:]
                if deleted_s == deleted_s[::-1] or deleted_reverse == deleted_reverse[::-1]:
                    return True
                
                return False