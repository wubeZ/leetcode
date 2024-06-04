class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        
        if len(counter) == 1:
            return len(s)
        
        even = 0
        odd = 0
        
        for key, val in counter.items():
            if val % 2 != 0:
                even += val - 1
                odd += 1
            else:
                even += val
        
        if odd >= 1:
            return even + 1
        
        return even
                
        
        
                