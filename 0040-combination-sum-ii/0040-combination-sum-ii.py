class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        def dfs(idx, total):
            if total > target:
                return 
            
            if total == target:
                ans.add(tuple(path))
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i-1] == candidates[i]:
                    continue
                    
                path.append(candidates[i])
                total += candidates[i]
                
                dfs(i + 1, total)
                
                path.pop()
                total -= candidates[i]
                
        
        path = []
        ans = set()
        dfs(0, 0)
        
        return ans