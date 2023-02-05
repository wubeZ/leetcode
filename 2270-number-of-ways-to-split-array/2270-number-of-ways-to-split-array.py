class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [nums[-1]]
        for i in range(len(nums)-2,-1,-1):
            prefix.append(prefix[-1] + nums[i])
        
        prefix = prefix[::-1]
        
        ans = 0
        cur = 0
        for i in range(len(nums)-1):
            cur += nums[i]
            if cur >= prefix[i+1]:
                ans += 1
        
        return ans