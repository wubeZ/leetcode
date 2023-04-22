class Solution:
    def minInsertions(self, s: str) -> int:
        s1 = s[::-1]
        dp = [[0]*(len(s1)+1) for i in range(len(s)+1)]
        
        for i in range(len(s)):
            for j in range(len(s1)): 
                if s[i] == s1[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        
        return len(s) - dp[-1][-1]