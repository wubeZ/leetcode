class Solution:
    def solve(self, board: List[List[str]]) -> None:
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        m = len(board)
        n = len(board[0])
        in_bound = lambda row,col : 0 <= row < m and 0 <= col < n
        visited = set()
        
        def dfs(row ,col):
            for dir in direction:
                newrow ,newcol = row + dir[0] ,col + dir[1]
                
                if (newrow, newcol) not in visited and in_bound(newrow , newcol) \
                and board[newrow][newcol] == 'O':
                    visited.add((newrow,newcol))
                    dfs(newrow,newcol)
        
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (i in (0, m - 1) or j in (0, n -1)) and ((i,j) not in visited \
                and board[i][j] =='O'):
                    visited.add((i,j))
                    dfs(i,j)
        
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (i,j) not in visited and board[i][j] =='O':
                    board[i][j] = 'X'
                    
        return board