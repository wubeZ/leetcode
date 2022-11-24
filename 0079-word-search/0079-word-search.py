class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        inbound = lambda x,y: 0<= x < len(board) and 0 <= y < len(board[0])
        
        def dfs(r,c, idx):
            if idx == len(word):
                ans[0] = True
                return
            
            for dx, dy in direction:
                nr, nc = r + dx, c + dy
                if inbound(nr, nc) and board[nr][nc] == word[idx] and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    dfs(nr, nc, idx+1)
                    visited.remove((nr, nc))
                    
            return  ans
        
        ans = [False]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = set()
                    visited.add((i,j))
                    dfs(i,j,1)
                    if ans[0]:
                        return True
                    
        
        return False
        
            
        
        