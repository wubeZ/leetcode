class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mostFreq = 0
        counter = defaultdict(int)
        ans = 0
        l = 0 
        
        for r in range(len(s)):
            counter[s[r]] += 1
            mostFreq = max(mostFreq, counter[s[r]])
            
            while (r - l + 1 - mostFreq) > k:
                counter[s[l]] -= 1
                l += 1
                
            ans = max(ans , r - l + 1)
            
        return ans