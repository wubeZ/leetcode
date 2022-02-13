class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        window = 0
        count = 0
        while left <len(s):
            d = {}
            while (left + window) < len(s) and s[left + window] not in d:
                d[s[left + window]] = 1
                window += 1
            count = max(count, window)
            left += 1
            window = 0
        return count