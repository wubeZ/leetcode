class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def dfs(idx,path):
            if idx > len(nums): return
            
            ans.append(path)
            
            for i in range(idx, len(nums)):
                if i != idx and nums[i] == nums[i-1]:
                    continue
                dfs(i+1, path + [nums[i]])
        
        dfs(0,[])
        
        return ans
            
            