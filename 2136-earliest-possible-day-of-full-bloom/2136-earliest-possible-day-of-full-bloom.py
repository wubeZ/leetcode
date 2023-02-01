class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        time = list(zip(growTime, plantTime))
        
        time.sort(reverse = True)
        ans = 0
        cur_time = 0
        
        for g_time, p_time in time:
            cur_time += p_time
            ans = max(ans, cur_time + g_time)
        
        return ans