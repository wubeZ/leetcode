class Solution:
    
    def isSolved(self, board):
        rowCheck = defaultdict(set)
        colCheck = defaultdict(set)
        boxCheck = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                if board[i][j] in rowCheck[i] or board[i][j] in colCheck[j] \
                or board[i][j] in boxCheck[(i//3,j//3)]:
                    return False
                
                rowCheck[i].add(board[i][j])
                colCheck[j].add(board[i][j])
                boxCheck[(i//3,j//3)].add(board[i][j]) 

        return True
            
    def backtrack(self, row, col, board):
            if row == 9:
                if self.isSolved(board):
                    return True
                return False
            
            if board[row][col] == ".":
                for num in "123456789":
                    if num not in self.rows[row] and num not in self.cols[col] \
                    and num not in self.squares[(row//3, col//3)]:
                        board[row][col] = num
                        self.rows[row].add(board[row][col])
                        self.cols[col].add(board[row][col])
                        self.squares[(row//3, col//3)].add(board[row][col])
                        
                        if col < 8:
                            checker = self.backtrack(row, col + 1, board)
                        else:
                            checker = self.backtrack(row + 1, 0, board)
                        
                        if checker:
                            return True
                        
                        self.rows[row].remove(board[row][col])
                        self.cols[col].remove(board[row][col])
                        self.squares[(row//3, col//3)].remove(board[row][col])
                        board[row][col] = "."
            else:
                
                if col < 8:
                    checker = self.backtrack(row, col + 1, board)
                else:
                    checker = self.backtrack(row + 1, 0, board)
                    
                if checker:
                    return True
                
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        self.rows = defaultdict(set)
        self.cols = defaultdict(set)
        self.squares = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    self.rows[i].add(board[i][j])
                    self.cols[j].add(board[i][j])
                    self.squares[(i//3, j//3)].add(board[i][j])

                    
        self.backtrack(0, 0, board)