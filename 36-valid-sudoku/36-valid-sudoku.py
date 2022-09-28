class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowCheck = defaultdict(set)
        colCheck = defaultdict(set)
        boxCheck = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                if board[i][j] not in rowCheck[i] and board[i][j] not in colCheck[j] and board[i][j] not in boxCheck[(i//3,j//3)]:
                    rowCheck[i].add(board[i][j])
                    colCheck[j].add(board[i][j])
                    boxCheck[(i//3,j//3)].add(board[i][j]) 
                else: 
                    return False
        return True
            
            
            
        