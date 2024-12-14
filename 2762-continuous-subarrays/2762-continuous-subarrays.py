class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans = len(nums)
        
        wind = {nums[0]: 1}
        
        l, r = 0, 1
        
        while r < len(nums):
            wind[nums[r]] = wind.get(nums[r], 0) + 1
            
            while (max(wind) - min(wind)) > 2:
                wind[nums[l]] -= 1
                if wind[nums[l]] == 0:
                    del wind[nums[l]]
                l += 1
            
            ans += r - l
                
            r += 1
                
        
        
        return ans