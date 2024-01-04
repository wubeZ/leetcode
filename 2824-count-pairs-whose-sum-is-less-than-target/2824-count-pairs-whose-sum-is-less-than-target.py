class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        left = 0
        right = len(nums)-1
        
        count = 0
        
        while left < right:
            if nums[left] + nums[right] >= target:
                right -= 1
                count += left
            else:
                left += 1
        
        count += (left* (left + 1))//2
        
        return count