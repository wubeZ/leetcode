class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i > j:
                return 0
            count = 0
            if s[i] == s[j]:
                if i == j:
                    count += dfs(i+1, j-1) + 1
                else:
                    count += dfs(i+1, j-1) + 2
            else:
                count += max(dfs(i+1, j), dfs(i, j-1))
            memo[(i,j)] = count
            return memo[(i,j)]
        
        return dfs(0, len(s)-1)