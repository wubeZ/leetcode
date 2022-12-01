class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        inbound = lambda x,y: 0<=x < len(matrix) and 0<= y < len(matrix[0])
        
        def dfs(r,c, direction):
            nr, nc = r + direction[0], c + direction[1]
            if inbound(nr, nc) and matrix[nr][nc] != 0:
                matrix[nr][nc] = float("inf")
                dfs(nr, nc, direction)

        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0 :
                    dfs(i,j, [1,0])
                    dfs(i,j, [-1,0])
                    dfs(i,j , [0,1])
                    dfs(i,j, [0,-1])
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0
    