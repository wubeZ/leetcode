class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = [0]
        def solve(i, path):
            if i >= len(arr):
                if len(set(path)) == len(path):
                    ans[0] = max(ans[0], len(path))
                return 
            
            if len(path) == len(set(path)):
                solve(i + 1, path)
                solve(i + 1, path + list(arr[i]))       
        
        
        solve(0, [])
        
        return ans[0]