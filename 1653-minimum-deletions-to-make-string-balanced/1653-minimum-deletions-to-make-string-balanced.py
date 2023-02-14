class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count = 0
        b_count = 0
        for i in range(len(s)):
            if s[i] == "a":
                a_count += 1
        b_count = len(s) - a_count
        
        ans = min(a_count, b_count)
        
        temp = sorted(s)
        temp = "".join(temp[::-1])
        if temp == s:
            return ans
        
        cur_a = 0
        cur_b = 0
        
        for i in range(len(s)):
            left_a = a_count - cur_a
            ans = min(ans, left_a + cur_b)
            
            if s[i] == "a":
                cur_a += 1
            else:
                cur_b += 1
        
        return ans