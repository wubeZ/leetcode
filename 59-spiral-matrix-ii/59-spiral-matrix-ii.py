class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for i in range(n)]
        i, j, idx, jdx = 0, 0, 0, 1
        
        for val in range(1, (n*n)+ 1):
            ans[i][j] = val

            if ans[(i + idx) % n][(j + jdx) % n] != 0:
                temp = idx
                idx = jdx
                jdx = -temp
            
            i += idx
            j += jdx
            
        
        return ans