class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        total = sum(nums)
        
        ans = 0
        maxval = float("inf")
        left = 0
        for i in range(len(nums)):
            left += nums[i]
            right = total - left
            x = left//(i+1) if left != 0 else 0 
            y = right//(len(nums)-i-1) if right != 0 else 0
            val = abs(x-y)
            if maxval > val:
                maxval = val
                ans = i
        
        return ans
        