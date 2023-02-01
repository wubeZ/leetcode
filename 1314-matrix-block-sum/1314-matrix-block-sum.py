class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        prefix = [[0]*(m + 1) for i in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1,m + 1):
                prefix[i][j] = prefix[i][j-1] + mat[i-1][j-1]
        
        for j in range(1,m + 1):
            for i in range(1,n + 1):
                prefix[i][j] += prefix[i-1][j]
        
        ans  = [[0] * m for i in range(n)]
            
        for i in range(n):
            for j in range(m):
                row1, col1 = i - k, j - k
                if row1 < 0: row1 = 0
                if col1 < 0: col1 = 0
                
                row2, col2 = i + k, j + k
                if row2 >= n: row2 = n - 1
                if col2 >= m: col2 = m - 1
                
                value = (prefix[row2+1][col2+1] - prefix[row1][col2+1]) - (prefix[row2+1][col1] - prefix[row1][col1])
                
                ans[i][j] = value
                
        return ans
                