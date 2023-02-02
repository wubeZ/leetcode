class Solution:
    def numberOfWays(self, s: str) -> int:
        
        total_ones = 0
        for i in s:
            if i == "1":
                total_ones += 1
        total_zeros = len(s) - total_ones
        
        ans = 0
        cur_ones = 0
        cur_zeros = 0
        
        if s[0] == "1":
            cur_ones += 1
        else:
            cur_zeros += 1
        
        for i in range(1,len(s)):
            if s[i] == "1":
                left_zeros = total_zeros - cur_zeros
                ans += cur_zeros * left_zeros
                cur_ones += 1    
            else:
                left_ones = total_ones - cur_ones
                ans += cur_ones * left_ones
                cur_zeros += 1
        
        return ans
