class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0]*(len(s2)+1) for i in range(len(s1)+1)]
        total = 0
        for i in range(len(s1)-1,-1,-1):
            total += ord(s1[i]) 
            dp[i][len(s2)] = total
            
        total = 0    
        for j in range(len(s2)-1,-1,-1):
            total += ord(s2[j]) 
            dp[len(s1)][j] = total

        for i in range(len(s1)-1,-1,-1):
            for j in range(len(s2)-1,-1,-1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j] + ord(s1[i]), dp[i][j+1] + ord(s2[j]))
        
        return dp[0][0]
        