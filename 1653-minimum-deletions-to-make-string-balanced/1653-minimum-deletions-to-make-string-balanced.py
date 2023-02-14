class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans = 0
        b_count = 0
        
        for ch in s:
            if ch == "b":
                b_count += 1
                
            elif b_count > 0:
                b_count -= 1
                ans += 1
        
        return ans
                