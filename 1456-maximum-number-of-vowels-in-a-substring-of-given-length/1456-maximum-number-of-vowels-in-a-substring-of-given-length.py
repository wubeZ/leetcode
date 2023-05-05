class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = 0
        l = 0
        count = 0
        vowels = "aeiou"
        
        for r in range(len(s)):
            if s[r] in vowels:
                count += 1
            while (r-l+1) == k:
                ans = max(ans, count)
                if s[l] in vowels:
                    count -= 1
                l += 1
        
        return ans