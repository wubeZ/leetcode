class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(idx, total):
            if idx >= len(candidates) or total > target:
                return
            
            if total == target:
                ans.append(path[::])
                return
            
            for i in range(idx, len(candidates)):
                total += candidates[i]
                path.append(candidates[i])
                dfs(i, total)
                total -= candidates[i]
                path.pop()
                
        ans = []
        path = []
        dfs(0, 0)
        
        return ans