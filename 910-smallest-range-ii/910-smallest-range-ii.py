class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = nums[-1] - nums[0]
        minn = nums[0] + k
        maxx = nums[-1] -k
        
        for i in range(1,len(nums)):
            left = min(minn, nums[i] - k)
            right = max(maxx, nums[i-1] + k)
            
            res = min(res, right - left)
        
        return res