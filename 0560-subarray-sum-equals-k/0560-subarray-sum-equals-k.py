class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        maps = defaultdict(int)
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(prefix[-1] + nums[i])
        
        running = 0
        ans = 0
        maps[0] = 1
        for i in range(len(prefix)):
            if prefix[i] - k in maps:
                ans += maps[prefix[i] - k]
            maps[prefix[i]] += 1
        
        return ans