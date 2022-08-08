class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        def backtrack(candidates, path, total):
            if total > target:
                return 
            
            if total == target:
                result.append(path)
                return
    
            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i-1]:
                    continue
                    
                backtrack(candidates[i+1:], path + [candidates[i]], total +  candidates[i])
                
        result = []
        backtrack(candidates, [], 0)
            
        return result