class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        arr = list(zip(ages, scores))
        arr.sort(reverse = True)
        
        ans = 0
        dp = [0]*n
        
        for i in range(n):
            score = arr[i][1]
            dp[i] = score
            for j in range(i):
                if arr[j][1] >= arr[i][1]:
                    dp[i] = max(dp[i], dp[j] + score)
                    
            ans = max(ans, dp[i])
        
        return ans
        