class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i for i in range(1,10)]
        def backtrack(nums, path):
            
            if len(path) > k: return 
            
            if len(path) == k and sum(path) == n:
                result.append(path)
            
            
            for i in range(len(nums)):
                backtrack(nums[i+1:], path + [nums[i]])
            
            
        result = []
        backtrack(nums, [])
        
        return result