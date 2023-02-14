class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans = 0
        b_stack = []
        
        for ch in s:
            if ch == "b":
                b_stack.append(ch)
            elif b_stack:
                b_stack.pop()
                ans += 1
        
        return ans
                