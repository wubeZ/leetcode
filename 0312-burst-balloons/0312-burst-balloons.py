class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        memo = {}
        nums = [1] + nums + [1]
        
        def dfs(l, r):

            if l > r:
                return 0

            if (l, r) in memo:
                return memo[(l, r)]
            
            answer = 0
            for k in range(l, r+1):
                answer = max(answer, dfs(l, k-1) + (nums[k]*nums[l-1]*nums[r+1]) + dfs(k+1, r))
            
            memo[(l, r)]= answer
            return memo[(l, r)]
        

        return dfs(1, len(nums)-2)