class Solution:
    def maxDepth(self, s: str) -> int:
        
        stack = 0
        ans = 0
        
        for i in range(len(s)):
            if s[i] not in "()":
                continue
            
            if s[i] == "(":
                stack += 1
            else:
                stack -= 1
            
            ans = max(ans, stack)
            
        
        
        return ans
            