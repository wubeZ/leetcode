class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                ans += 1
        
        i = 0
        while i < len(nums):
            
            j = i
            count = 0
            while j < len(nums) and nums[j] == 0:
                count += 1
                if count > 1:
                    ans += count - 1
                j += 1
                
            i = j
            i += 1
            
        
        return ans