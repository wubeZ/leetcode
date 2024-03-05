class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        
        ans = []
        def dfs(i,idx, path):
        
            if len(path) == len(digits) and path:
                ans.append("".join(path))
                return
            
            if idx >= len(digits):
                return
            
            for j in range(len(hashmap[int(digits[idx]) - 2])):
                dfs(j + 1, idx + 1,  path + [hashmap[int(digits[idx]) - 2][j]])
                
        
        
        
        dfs(0,0, [])
        
        return ans