class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        count = 0
        s = list(s)
        prev = 0
        ans = 0
        while True:
            i = 1
            while i < len(s):
                if s[i-1] == "0" and s[i] == "1":
                    s[i-1], s[i] = s[i], s[i-1]
                    count += 1
                    i += 2
                else:
                    i += 1
            
            if count == prev:
                break
            ans += 1
            prev = count
                    
        return ans