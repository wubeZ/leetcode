class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        inbound = lambda x,y: 0<= x < len(heights) and 0<= y < len(heights[0])
    
        def dfs(r, c, visited):
            visited.add((r,c))
            for dx, dy in direction:
                nr, nc = r + dx, c + dy
                if inbound(nr,nc) and (nr,nc) not in visited and heights[r][c] <= heights[nr][nc]:
                    dfs(nr, nc, visited)
        aset = set()
        pset = set()
        
        for i in range(len(heights)):
            dfs(i, 0, pset)
            dfs(i, len(heights[0])-1, aset)
            
        for j in range(len(heights[0])):
            dfs(0, j, pset)
            dfs(len(heights)-1, j, aset)
        
        return aset & pset