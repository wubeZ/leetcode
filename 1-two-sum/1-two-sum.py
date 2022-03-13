class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i ,val in enumerate(nums):
            diff = target - val
            
            if diff in seen:
                return [seen[diff],i]
            
            seen[val] = i
        