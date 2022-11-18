class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        ans = 1
        numset = set(nums)
        
        for i in range(len(nums)):
            if nums[i]-1 not in numset:
                count = 1
                num = nums[i]
                while num + 1 in numset:
                    count += 1
                    num += 1
                ans = max(ans, count)
        
        return ans
            