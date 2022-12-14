class Solution:
    def numberOfWays(self, s: str) -> int:
        num_ones = 0
        for ch in s:
            if ch == '1':
                num_ones += 1
        
        count = 0
        cur_ones = 0
        num_zeros = len(s) - num_ones
        for i in range(len(s)):
            if s[i] == '1':
                cur_ones += 1
                cur_zeros = (i + 1) - cur_ones
                count += (cur_zeros) * (num_zeros - cur_zeros)
            else:
            
                count += (cur_ones) * (num_ones - cur_ones)
        
        return count