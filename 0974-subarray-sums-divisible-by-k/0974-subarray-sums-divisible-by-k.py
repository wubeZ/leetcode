class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        prefix = [0]
        maps = defaultdict(int)
        
        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])
        
        maps[0] = 1
        for i in range(1,len(prefix)):
            if prefix[i]%k in maps:
                ans += maps[prefix[i]%k]
            maps[prefix[i]%k] += 1
            
        return ans