class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(path, left, right):
            if len(path)//2 == n:
                result.append("".join(path))
                return 
            
            if left < n:
                backtrack(path + ["("], left + 1, right)
            if right < left:
                backtrack(path + [")"], left, right + 1)
        
        
        result = []
        
        backtrack([],0,0)
        
        return result
        
        
        
            
            
            
            