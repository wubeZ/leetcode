class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans = [[0 for i in range(len(grid)-2)] for i in range(len(grid)-2)]
        
        for i in range(len(grid)-2):
            for j in range(len(grid)-2):
                maxx = 0
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        maxx = max(maxx, grid[k][l])
                ans[i][j] = maxx
            
        return ans