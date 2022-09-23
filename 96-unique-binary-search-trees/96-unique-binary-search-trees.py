class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1 for i in range(n + 1)]
        dp[1] = 1
        
        for i in range(2, n+1):
            temp = 0
            for j in range(1, i + 1):
                temp += (dp[j-1] * dp[i-j])
            dp[i] = temp
        
        return dp[n]
        