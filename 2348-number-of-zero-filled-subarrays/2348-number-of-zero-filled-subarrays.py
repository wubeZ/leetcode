class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        
        i = 0
        while i < len(nums):
            
            j = i
            count = 0
            while j < len(nums) and nums[j] == 0:
                count += 1
                ans += count
                j += 1
                
            i = j
            i += 1
            
        
        return ans