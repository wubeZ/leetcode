class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def solve(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i >= len(text1) or j >= len(text2):
                return 0
            count = 0
            if text1[i] == text2[j]:
                count = solve(i+1, j+1) + 1
            else:
                count += max(solve(i + 1,j), solve(i, j + 1))
            memo[(i,j)] = count
            return memo[(i,j)]
        
        return solve(0,0)