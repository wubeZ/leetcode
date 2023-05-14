class Solution:
    def maxScore(self, nums: List[int]) -> int:
        memo = {}
        def dfs(nums, op):
            if nums in memo:
                return memo[nums]
            
            score = 0            
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    new_nums = nums[:i] + nums[i+1:j] + nums[j+1:]
                    score = max(score, op * gcd(nums[i], nums[j]) + dfs(new_nums , op+1))
            
            memo[nums] = score
            return memo[nums]
        
        return dfs(tuple(nums), 1)