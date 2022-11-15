class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        ans = 0
        while l < len(nums) and r < len(nums):
            ans = l
            if nums[l] < nums[r]:
                nums[l+1],nums[r] = nums[r], nums[l+1]
                l += 1
                r = l
            else:
                r += 1
        
        return ans + 1
                