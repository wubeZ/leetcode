class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)-1
        while l > 0:
            if nums[l] > nums[l-1]:
                r = l
                while r < len(nums) and nums[r] > nums[l-1]:
                    r += 1
                nums[r-1], nums[l-1] = nums[l-1], nums[r-1]
                nums[l:] = sorted(nums[l:])
                return
            l -= 1
        nums.reverse()
        
        