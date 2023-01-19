class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        prefix = 0
        maps = {}
        
        maps[0] = 1
        for i in range(len(nums)):
            prefix += nums[i]
            ans += maps.get(prefix % k , 0)
            maps[prefix % k] = maps.get(prefix % k, 0) + 1
            
        return ans