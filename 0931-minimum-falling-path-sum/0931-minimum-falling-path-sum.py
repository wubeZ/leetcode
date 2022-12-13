class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo = {}
        def solve(i,j):
            if i >= len(matrix):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            count1, count2, count3 = float('inf'), float('inf'), float('inf')
            if j-1 >= 0:
                count1 = solve(i+1,j-1)
            if j < len(matrix):
                count2 = solve(i+1,j)
            if j+1 < len(matrix):
                count3 = solve(i+1,j+1)
            memo[(i,j)] = min(count1, count2, count3) + matrix[i][j]

            return memo[(i,j)]
        
        ans = float('inf')
        for j in range(len(matrix)):
            val = solve(0,j)
            ans = min(ans, val)
        return ans