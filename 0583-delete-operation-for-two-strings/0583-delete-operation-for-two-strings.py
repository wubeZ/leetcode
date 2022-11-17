class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i >= len(word1) or j >= len(word2):
                return 0
            count = 0
            if word1[i] == word2[j]:
                count += dfs(i+1, j+1) + 1
            else:
                count += max(dfs(i+1,j), dfs(i, j+1))
            memo[(i,j)] = count
            return memo[(i,j)]
        
        val = dfs(0,0)
        
        return len(word1) + len(word2) - 2 * val