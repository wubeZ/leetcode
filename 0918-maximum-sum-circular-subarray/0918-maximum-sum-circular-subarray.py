class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        min_total = nums[0]
        max_total = nums[0]
        cur_min = 0
        cur_max = 0
        total = 0
        for i in range(len(nums)):
            cur_min = min(0, cur_min) + nums[i]
            cur_max = max(0, cur_max) + nums[i]
            min_total = min(min_total, cur_min)
            max_total = max(max_total, cur_max)
            total += nums[i]
        
        if total == min_total:
            return max_total
        return max(max_total, total - min_total)