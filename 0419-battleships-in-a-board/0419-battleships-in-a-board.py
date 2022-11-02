class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        directions = [[-1,0],[0,1]]
        inbound = lambda x,y : 0 <= x < len(board) and 0 <= y < len(board[0])
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    c = 0
                    for dx,dy in directions:
                        ni, nj = i + dx, j + dy
                        if inbound(ni,nj) and board[ni][nj] == "X":
                            c += 1        
                    if c == 0:        
                        count += 1
        return count 
                    