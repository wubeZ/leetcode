class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        memo = {}
        
        def dfs(idx, k):
            if idx >= len(piles):
                return 0
            
            cur_max, total = 0, 0
            
            if (idx, k) in memo:
                return memo[(idx, k)]
            
            cur_max = max(cur_max, dfs(idx + 1, k))
        
            for j in range(len(piles[idx])):
                total += piles[idx][j]
                left = k - (j + 1)
                if left >= 0:
                    cur_max = max(cur_max, total + dfs(idx + 1, left))
                
            memo[(idx, k)] = cur_max
            
            return memo[(idx, k)]
        
        return dfs(0, k)
                    