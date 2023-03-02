class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        ans = 0
        maps = defaultdict(int)
        distinct = 1
        
        for right in range(len(s)):
            maps[s[right]] += 1
            if maps[s[right]] == 2:
                distinct = 2
                
            while distinct == 2:
                if maps[s[left]] == 2:
                    distinct -= 1
                maps[s[left]] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
                
        
        return ans