class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visited = set()
        def backtrack(nums, path):
            if len(path) == n:
                path_ = tuple(path)
                if path_ not in visited:
                    visited.add(path_)
                    result.append(path)
                return
            
            for i in range(len(nums)):
                backtrack(nums[:i] +nums[i+1:], path + [nums[i]])
            
        
        
        result = []
        
        backtrack(nums, [])
        
        return result