class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        prefixRow = [[0]*(m+1) for i in range(n+1)] 
        prefixCol = [[0]*(m+1) for i in range(n+1)]
        
        for i in range(n):
            for j in range(m):
                prefixRow[i][j] = prefixRow[i][j-1] + grid[i][j]
                prefixCol[i][j] = prefixCol[i-1][j] + grid[i][j]
        
        
        ans = 1
        for i in range(n):
            for j in range(m):
                for length in range(2, min(n-i,m-j)+1):
                    totalsum = prefixRow[i][j+length-1] - prefixRow[i][j-1]
                    flag = True
                    dig, antidig = 0 ,0 
                    for l in range(length):
                        row = prefixRow[i+l][j+length-1] - prefixRow[i+l][j-1]
                        if row != totalsum:
                            flag = False
                            break
                        col = prefixCol[i+length-1][j+l] - prefixCol[i-1][j+l]
                        if col != totalsum:
                            flag = False
                            break
                        dig += grid[i+l][j+l]
                        antidig += grid[i+l][j+length-1-l]
                
                    if flag and dig == antidig == totalsum:
                        ans = max(ans, length)
        
        return ans