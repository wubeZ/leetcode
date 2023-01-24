class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        ROWS, COLS = len(board), len(board[0])
        sq = ROWS * ROWS
        
        def findIndex(num):
            row = ROWS - ((num - 1) // COLS) - 1
            mod = (num - 1) % COLS
            col = 0
            
            if (ROWS - row) % 2 == 0:
                col = COLS - mod - 1
            else:
                col = mod
            return (row, col)
    
        queue = deque()
        visited = set()
        queue.append((1, 0))
        
        while queue:
            n = len(queue)
            
            for i in range(n):
                cur,level = queue.popleft()
                
                for j in range(1, 7):
                    val = min(cur + j, sq)
                     
                    r, c = findIndex(val)
                    if board[r][c] != -1:
                        val = board[r][c]
                    
                    if val == sq:
                        return level + 1
                    
                    if val not in visited:
                        visited.add(val)
                        queue.append((val, level + 1))
                    
            
        return -1