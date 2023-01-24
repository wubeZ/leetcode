class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        cells = defaultdict(tuple)
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
        ans = float('inf')
        while queue:
            n = len(queue)
            
            for i in range(n):
                cur,level = queue.popleft()
                
                if cur == sq:
                    ans = min(ans, level)
                
                for j in range(1, 7):
                    val = min(cur + j, sq)
                    if val in visited:
                        continue
                     
                    r, c = findIndex(val)
                    if board[r][c] == -1:
                        queue.append((val, level + 1))
                    else:
                        queue.append((board[r][c], level + 1))
                        
                    visited.add(val)
                
        if ans == float('inf'):
            ans = -1
            
        return ans