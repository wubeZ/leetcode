class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        d = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        def backtrack(idx, path):
            if idx >= len(digits):
                if len(path) != 0:
                    result.append("".join(path))
                return
            
            for char in d[digits[idx]]:
                path.append(char)
                backtrack(idx +1, path)
                path.pop()
        
                
        result = []
        backtrack(0,[])
        return result
            
            