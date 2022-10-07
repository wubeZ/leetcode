class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(nums, path):
            if sum(path) > target:
                return
            if sum(path) == target:
                res.append(path)
                return 
            
            for i in range(len(nums)):
                dfs(nums[i:], path + [nums[i]])
        
        dfs(candidates, [])
        
        return res