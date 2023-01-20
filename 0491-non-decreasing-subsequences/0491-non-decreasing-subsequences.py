class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = set()
        path = []

        def backtrack(idx, path):
            if idx == len(nums):
                if len(path) >= 2:
                    result.add(tuple(path))
                return
            
            if not path or path[-1] <= nums[idx]:
                backtrack(idx + 1, path + [nums[idx]])
            
            backtrack(idx + 1, path)
            
        backtrack(0, path)
        
        return result