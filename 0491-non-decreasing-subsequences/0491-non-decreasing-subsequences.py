class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = set()
        path = []

        def backtrack(idx):
            if idx == len(nums):
                if len(path) >= 2:
                    result.add(tuple(path))
                return
            
            if not path or path[-1] <= nums[idx]:
                path.append(nums[idx])
                backtrack(idx + 1)
                path.pop()
                
            backtrack(idx + 1)
            
        backtrack(0)
        
        return result