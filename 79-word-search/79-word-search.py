class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        in_bound = lambda x,y: 0 <= x < len(board) and 0 <= y < len(board[0])
        direction = [[1,0], [0,1], [-1,0], [0,-1]]
        
        
        def backtrack(r, c, idx, visited):
            if len(word) == idx:
                return True
            
            for pair in direction:
                nr, nc = r + pair[0], c + pair[1]
                if in_bound(nr,nc) and (nr,nc) not in visited and word[idx] == board[nr][nc]:
                    visited.add((nr, nc))
                    if backtrack(nr, nc, idx + 1, visited):
                        return True
                    visited.remove((nr, nc))
                
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    visited = {(i,j)}
                    if backtrack(i, j, 1, visited):
                        return True
        
        return False