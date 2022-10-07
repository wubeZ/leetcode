class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def dfs(num, path):
            if len(path) == n:
                ans.append(path)
                return
            
            for i in range(len(num)):
                dfs(num[:i] + num[i+1:], path + [num[i]])
        
        dfs(nums, [])
        
        return ans