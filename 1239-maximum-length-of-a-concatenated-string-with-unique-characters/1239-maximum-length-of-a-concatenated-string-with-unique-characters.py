class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = [0]
        def solve(i, path):
            if i >= len(arr):
                word = "".join(path)
                if len(set(word)) == len(word):
                    ans[0] = max(ans[0], len(word))
                return 
            solve(i + 1, path)
            solve(i + 1, path + [arr[i]])       
        
        
        solve(0, [])
        
        return ans[0]