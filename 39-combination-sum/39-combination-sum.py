class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(idx, path):
            total = sum(path)
            if total == target:
                result.append(path)
                return
            
            for j in range(idx, len(candidates)):
                if total + candidates[j] <= target: 
                    backtrack(j, path + [candidates[j]])

            
        
        result = []
        
        backtrack(0,[])
        
        return result