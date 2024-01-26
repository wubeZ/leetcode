class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10**9 + 7
        in_bound = lambda x, y : 0 <= x < m and 0 <= y < n
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        memo = {}
        
        def solve(r, c, move):
            if not in_bound(r, c):
                return 1
            
            if move == 0:
                return 0
            
            if (r, c, move) in memo:
                return memo[(r, c, move)]
            
            total = 0
            for dx, dy in direction:
                nr, nc = r + dx, c + dy
                total += solve(nr, nc, move - 1)
            
            memo[(r, c, move)] = total
            
            return total
        
        return solve(startRow, startColumn, maxMove) % mod
            