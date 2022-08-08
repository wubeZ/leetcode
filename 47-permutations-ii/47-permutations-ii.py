class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        
        def backtrack(nums, path):
            if len(path) == n:
                result.append(path)
                return
            
            for i in range(len(nums)):
                
                if i > 0 and nums[i-1] == nums[i]:
                    continue
                backtrack(nums[:i] +nums[i+1:], path + [nums[i]])
            
        
        
        result = []
        
        backtrack(nums, [])
        
        return result