class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        in_grid = lambda x,y: 0 <= x < m and 0 <= y < n
        guarded = set()
        walls = set([(i,j) for i,j in walls])
        guards =  set([(i,j) for i,j in guards]) 
        
        def check(row, col, x, y):
            nr, nc = row + x, col + y
            while in_grid(nr, nc):
                if (nr,nc) not in walls and (nr,nc) not in guards:
                    guarded.add((nr,nc))
                    nr += x
                    nc += y
                else:
                    break
        
        
        for r, c in guards:
        
            for x,y in directions:
                check(r, c, x, y)
                
        
        return n*m - len(guarded) -len(walls) - len(guards)
        
            
            
            
            
                
        
        
            
        