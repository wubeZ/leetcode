class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        direction = [[0,1],[1,0],[-1,0],[0,-1]]
        in_bound = lambda x, y: 0 <= x < m and 0 <= y < n
        memo = {}
        M = 10**9 + 7
        
        def find(row, col, moves):
            if not in_bound(row,col):
                return 1
            
            elif moves == 0:
                return 0
            
            elif (row, col, moves) in memo:
                return memo[(row, col, moves)]
            
            else:
                sums = 0
                for dx, dy in direction:
                    sums += find(row + dx, col + dy, moves - 1)
                memo[(row, col, moves)] = sums
                return sums
        
        return find(startRow, startColumn, maxMove) % M
        
    
        