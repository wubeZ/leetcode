class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0]*(len(word2)+1) for i in range(len(word1)+1)]
        for i in range(len(dp)):
            dp[i][-1] = len(word1) - i
        for i in range(len(dp[0])):
            dp[-1][i] = len(word2) - i
        
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i][j+1],dp[i+1][j],dp[i+1][j+1]) + 1
        
        return dp[0][0]