class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxFreq, left ,diff = 0 , 0 , 0
        
        for right in range(len(nums)):
            diff += (right - left) * (nums[right] - nums[right-1])
            
            while left < right and diff > k:
                diff -= (nums[right] - nums[left])
                left += 1  
                
            maxFreq = max(maxFreq, right-left + 1)
            
        return maxFreq