class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = []
        for i in s:
            if i.isalnum():
                pattern.append(i)
        
        l, r = 0, len(pattern)-1
        while l < r:
            if pattern[l].lower() == pattern[r].lower():
                l += 1
                r -= 1
            else:
                return False
        
        return True