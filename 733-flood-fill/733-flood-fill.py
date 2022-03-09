class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        neighbours = [[0,1],[1,0],[-1,0],[0,-1]]
        visited = set([(sr,sc)])
        n = len(image)
        m = len(image[0])
        
        def dfs(row,col):
            image[row][col] = newColor
            visited.add((row,col))
            
            for dir in neighbours:
                newrow , newcol = row + dir[0], col + dir[1]
                if (newrow,newcol) in visited or not in_bound(newrow,newcol) or image[newrow][newcol] != start_color:
                    continue
                dfs(newrow, newcol)
        in_bound = lambda row, col : 0 <= row < n and 0 <= col < m
        start_color = image[sr][sc]
        image[sr][sc] = newColor
        dfs(sr,sc)
        
        return image
        
        
                    
            