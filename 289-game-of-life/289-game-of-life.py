class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None: 
        directions = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[-1,-1],[1,-1]]
        in_bound = lambda row,col: 0 <= row < len(board) and 0 <= col < len(board[0])
        ans = [[0]*len(board[0]) for i in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    count = 0
                    for dir in directions:
                        ni, nj = i + dir[0], j + dir[1]
                        if in_bound(ni,nj) and board[ni][nj] == 1:
                            count += 1
                    if count == 3:
                        ans[i][j] = 1
                else:
                    count = 0
                    for dir in directions:
                        ni, nj = i + dir[0], j + dir[1]
                        if in_bound(ni,nj) and board[ni][nj] == 1:
                            count += 1
                    if count == 2 or count == 3:
                        ans[i][j] = 1
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = ans[i][j]
        
        